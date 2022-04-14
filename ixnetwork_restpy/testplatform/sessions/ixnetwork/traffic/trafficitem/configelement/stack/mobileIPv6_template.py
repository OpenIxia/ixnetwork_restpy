from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MobileIPv6(Base):
    __slots__ = ()
    _SDM_NAME = "mobileIPv6"
    _SDM_ATT_MAP = {
        "MobileIPv6PacketProtocol": "mobileIPv6.mobileIPv6Packet.protocol-1",
        "MobileIPv6PacketLength": "mobileIPv6.mobileIPv6Packet.length-2",
        "MobileIPv6PacketMhType": "mobileIPv6.mobileIPv6Packet.mhType-3",
        "MobileIPv6PacketReserved": "mobileIPv6.mobileIPv6Packet.reserved-4",
        "MobileIPv6PacketChecksum": "mobileIPv6.mobileIPv6Packet.checksum-5",
        "BindingRefreshRequestReserved": "mobileIPv6.mobileIPv6Packet.body.bindingRefreshRequest.reserved-6",
        "HomeTestInitReserved": "mobileIPv6.mobileIPv6Packet.body.homeTestInit.reserved-7",
        "HomeTestInitCookie": "mobileIPv6.mobileIPv6Packet.body.homeTestInit.cookie-8",
        "CareOfTestInitErserved": "mobileIPv6.mobileIPv6Packet.body.careOfTestInit.erserved-9",
        "CareOfTestInitCookie": "mobileIPv6.mobileIPv6Packet.body.careOfTestInit.cookie-10",
        "HomeTestNonceIndex": "mobileIPv6.mobileIPv6Packet.body.homeTest.nonceIndex-11",
        "HomeTestInitCookie": "mobileIPv6.mobileIPv6Packet.body.homeTest.initCookie-12",
        "HomeTestKeygenCookie": "mobileIPv6.mobileIPv6Packet.body.homeTest.keygenCookie-13",
        "CareOfTestNonceIndex": "mobileIPv6.mobileIPv6Packet.body.careOfTest.nonceIndex-14",
        "CareOfTestInitCookie": "mobileIPv6.mobileIPv6Packet.body.careOfTest.initCookie-15",
        "CareOfTestKeygenCookie": "mobileIPv6.mobileIPv6Packet.body.careOfTest.keygenCookie-16",
        "BindingUpdateSequence": "mobileIPv6.mobileIPv6Packet.body.bindingUpdate.sequence-17",
        "BindingUpdateABit": "mobileIPv6.mobileIPv6Packet.body.bindingUpdate.aBit-18",
        "BindingUpdateHBit": "mobileIPv6.mobileIPv6Packet.body.bindingUpdate.hBit-19",
        "BindingUpdateLBit": "mobileIPv6.mobileIPv6Packet.body.bindingUpdate.lBit-20",
        "BindingUpdateKBit": "mobileIPv6.mobileIPv6Packet.body.bindingUpdate.kBit-21",
        "BindingUpdateReserved": "mobileIPv6.mobileIPv6Packet.body.bindingUpdate.reserved-22",
        "BindingUpdateLifetime": "mobileIPv6.mobileIPv6Packet.body.bindingUpdate.lifetime-23",
        "BindingAckStatus": "mobileIPv6.mobileIPv6Packet.body.bindingAck.status-24",
        "BindingAckKBit": "mobileIPv6.mobileIPv6Packet.body.bindingAck.kBit-25",
        "BindingAckReserved": "mobileIPv6.mobileIPv6Packet.body.bindingAck.reserved-26",
        "BindingAckSequence": "mobileIPv6.mobileIPv6Packet.body.bindingAck.sequence-27",
        "BindingAckLifetime": "mobileIPv6.mobileIPv6Packet.body.bindingAck.lifetime-28",
        "BindingErrorStatus": "mobileIPv6.mobileIPv6Packet.body.bindingError.status-29",
        "BindingErrorReserved": "mobileIPv6.mobileIPv6Packet.body.bindingError.reserved-30",
        "BindingErrorHomeAddress": "mobileIPv6.mobileIPv6Packet.body.bindingError.homeAddress-31",
        "Pad1Type": "mobileIPv6.mobileIPv6Packet.optionsHolder.options.tlvOption.pad1.type-32",
        "PadNType": "mobileIPv6.mobileIPv6Packet.optionsHolder.options.tlvOption.padN.type-33",
        "PadNLength": "mobileIPv6.mobileIPv6Packet.optionsHolder.options.tlvOption.padN.length-34",
        "PadNData": "mobileIPv6.mobileIPv6Packet.optionsHolder.options.tlvOption.padN.data-35",
        "BindingRefreshAdviceType": "mobileIPv6.mobileIPv6Packet.optionsHolder.options.tlvOption.bindingRefreshAdvice.type-36",
        "BindingRefreshAdviceLength": "mobileIPv6.mobileIPv6Packet.optionsHolder.options.tlvOption.bindingRefreshAdvice.length-37",
        "BindingRefreshAdviceData": "mobileIPv6.mobileIPv6Packet.optionsHolder.options.tlvOption.bindingRefreshAdvice.data-38",
        "AlternateCareOfAddressType": "mobileIPv6.mobileIPv6Packet.optionsHolder.options.tlvOption.alternateCareOfAddress.type-39",
        "AlternateCareOfAddressLength": "mobileIPv6.mobileIPv6Packet.optionsHolder.options.tlvOption.alternateCareOfAddress.length-40",
        "AlternateCareOfAddressData": "mobileIPv6.mobileIPv6Packet.optionsHolder.options.tlvOption.alternateCareOfAddress.data-41",
        "NonceIndicesType": "mobileIPv6.mobileIPv6Packet.optionsHolder.options.tlvOption.nonceIndices.type-42",
        "NonceIndicesLength": "mobileIPv6.mobileIPv6Packet.optionsHolder.options.tlvOption.nonceIndices.length-43",
        "NonceIndicesHomeNonce": "mobileIPv6.mobileIPv6Packet.optionsHolder.options.tlvOption.nonceIndices.homeNonce-44",
        "NonceIndicesCareOfNonce": "mobileIPv6.mobileIPv6Packet.optionsHolder.options.tlvOption.nonceIndices.careOfNonce-45",
        "BindingAuthorizationDataType": "mobileIPv6.mobileIPv6Packet.optionsHolder.options.tlvOption.bindingAuthorizationData.type-46",
        "BindingAuthorizationDataLength": "mobileIPv6.mobileIPv6Packet.optionsHolder.options.tlvOption.bindingAuthorizationData.length-47",
        "BindingAuthorizationDataAuthenticator": "mobileIPv6.mobileIPv6Packet.optionsHolder.options.tlvOption.bindingAuthorizationData.authenticator-48",
        "OptionsHolderPad": "mobileIPv6.mobileIPv6Packet.optionsHolder.pad-49",
    }

    def __init__(self, parent, list_op=False):
        super(MobileIPv6, self).__init__(parent, list_op)

    @property
    def MobileIPv6PacketProtocol(self):
        """
        Display Name: Payload Protocol
        Default Value: 59
        Value Format: decimal
        Available enum values: HOPOPT, 0, ICMP, 1, IGMP, 2, GGP, 3, IP, 4, ST, 5, TCP, 6, CBT, 7, EGP, 8, IGP, 9, BBN-RCC-MON, 10, NVP-II, 11, PUP, 12, ARGUS, 13, EMCON, 14, XNET, 15, CHAOS, 16, UDP, 17, MUX, 18, DCN-MEAS, 19, HMP, 20, PRM, 21, XNS-IDP, 22, TRUNK-1, 23, TRUNK-2, 24, LEAF-1, 25, LEAF-2, 26, RDP, 27, IRTP, 28, ISO-TP4, 29, NETBLT, 30, MFE-NSP, 31, MERIT-INP, 32, SEP, 33, 3PC, 34, IDPR, 35, XTP, 36, DDP, 37, IDPR-CMTP, 38, TP++, 39, IL, 40, IPv6, 41, SDRP, 42, IPv6-Route, 43, IPv6-Frag, 44, IDRP, 45, RSVP, 46, GRE, 47, MHRP, 48, BNA, 49, ESP, 50, AH, 51, I-NLSP, 52, SWIPE, 53, NARP, 54, MOBILE, 55, TLSP, 56, SKIP, 57, IPv6-ICMP, 58, IPv6-NoNxt, 59, IPv6-Opts, 60, Any host internal protocol, 61, CFTP, 62, Any local network, 63, SAT-EXPAK, 64, KRYPTOLAN, 65, RVD, 66, IPPC, 67, Any distributed file system, 68, SAT-MON, 69, VISA, 70, IPCV, 71, CPNX, 72, CPHB, 73, WSN, 74, PVP, 75, BR-SAT-MON, 76, SUN-ND, 77, WB-MON, 78, WB-EXPAK, 79, ISO-IP, 80, VMTP, 81, SECURE-VMTP, 82, VINES, 83, TTP, 84, NSFNET-IGP, 85, DGP, 86, TCF, 87, EIGRP, 88, OSPFIGP, 89, Sprite-RPC, 90, LARP, 91, MTP, 92, AX.25, 93, IPIP, 94, MICP, 95, SCC-SP, 96, ETHERIP, 97, ENCAP, 98, Any private encryption, 99, GMTP, 100, IFMP, 101, PNNI, 102, PIM, 103, ARIS, 104, SCPS, 105, QNX, 106, A/N, 107, IPComp, 108, SNP, 109, Compaq-Peer, 110, IPX-in-IP, 111, VRRP, 112, PGM, 113, Any 0-hop protocol, 114, L2TP, 115, DDX, 116, IATP, 117, STP, 118, SRP, 119, UTI, 120, SMP, 121, SM, 122, PTP, 123, ISIS over IPv4, 124, FIRE, 125, CRTP, 126, CRUDP, 127, SSCOPMCE, 128, IPLT, 129, SPS, 130, PIPE, 131, SCTP, 132, FC, 133, RSVP-E2E-IGNORE, 134, Mobility Header, 135, UDPLite, 136, MPLS-in-IP, 137, Unassigned, 138, Unassigned, 139, Unassigned, 140, Unassigned, 141, Unassigned, 142, Unassigned, 143, Unassigned, 144, Unassigned, 145, Unassigned, 146, Unassigned, 147, Unassigned, 148, Unassigned, 149, Unassigned, 150, Unassigned, 151, Unassigned, 152, Unassigned, 153, Unassigned, 154, Unassigned, 155, Unassigned, 156, Unassigned, 157, Unassigned, 158, Unassigned, 159, Unassigned, 160, Unassigned, 161, Unassigned, 162, Unassigned, 163, Unassigned, 164, Unassigned, 165, Unassigned, 166, Unassigned, 167, Unassigned, 168, Unassigned, 169, Unassigned, 170, Unassigned, 171, Unassigned, 172, Unassigned, 173, Unassigned, 174, Unassigned, 175, Unassigned, 176, Unassigned, 177, Unassigned, 178, Unassigned, 179, Unassigned, 180, Unassigned, 181, Unassigned, 182, Unassigned, 183, Unassigned, 184, Unassigned, 185, Unassigned, 186, Unassigned, 187, Unassigned, 188, Unassigned, 189, Unassigned, 190, Unassigned, 191, Unassigned, 192, Unassigned, 193, Unassigned, 194, Unassigned, 195, Unassigned, 196, Unassigned, 197, Unassigned, 198, Unassigned, 199, Unassigned, 200, Unassigned, 201, Unassigned, 202, Unassigned, 203, Unassigned, 204, Unassigned, 205, Unassigned, 206, Unassigned, 207, Unassigned, 208, Unassigned, 209, Unassigned, 210, Unassigned, 211, Unassigned, 212, Unassigned, 213, Unassigned, 214, Unassigned, 215, Unassigned, 216, Unassigned, 217, Unassigned, 218, Unassigned, 219, Unassigned, 220, Unassigned, 221, Unassigned, 222, Unassigned, 223, Unassigned, 224, Unassigned, 225, Unassigned, 226, Unassigned, 227, Unassigned, 228, Unassigned, 229, Unassigned, 230, Unassigned, 231, Unassigned, 232, Unassigned, 233, Unassigned, 234, Unassigned, 235, Unassigned, 236, Unassigned, 237, Unassigned, 238, Unassigned, 239, Unassigned, 240, Unassigned, 241, Unassigned, 242, Unassigned, 243, Unassigned, 244, Unassigned, 245, Unassigned, 246, Unassigned, 247, Unassigned, 248, Unassigned, 249, Unassigned, 250, Unassigned, 251, Unassigned, 252, Unassigned, 253, Unassigned, 254, Reserved, 255
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MobileIPv6PacketProtocol"])
        )

    @property
    def MobileIPv6PacketLength(self):
        """
        Display Name: Header Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MobileIPv6PacketLength"])
        )

    @property
    def MobileIPv6PacketMhType(self):
        """
        Display Name: MH Type
        Default Value: 0
        Value Format: decimal
        Available enum values: Binding Refresh Request, 0, Home Test Init Message, 1, Care-of Test Init Message, 2, Home Test Message, 3, Care-of Test Message, 4, Binding Update Message, 5, Binding Ack Message, 6, Binding Error Message, 7
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MobileIPv6PacketMhType"])
        )

    @property
    def MobileIPv6PacketReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MobileIPv6PacketReserved"])
        )

    @property
    def MobileIPv6PacketChecksum(self):
        """
        Display Name: Checksum
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MobileIPv6PacketChecksum"])
        )

    @property
    def BindingRefreshRequestReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["BindingRefreshRequestReserved"]),
        )

    @property
    def HomeTestInitReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HomeTestInitReserved"])
        )

    @property
    def HomeTestInitCookie(self):
        """
        Display Name: Home Cookie
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HomeTestInitCookie"])
        )

    @property
    def CareOfTestInitErserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CareOfTestInitErserved"])
        )

    @property
    def CareOfTestInitCookie(self):
        """
        Display Name: Care-of Cookie
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CareOfTestInitCookie"])
        )

    @property
    def HomeTestNonceIndex(self):
        """
        Display Name: Home Nonce Index
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HomeTestNonceIndex"])
        )

    @property
    def HomeTestInitCookie(self):
        """
        Display Name: Home Init Cookie
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HomeTestInitCookie"])
        )

    @property
    def HomeTestKeygenCookie(self):
        """
        Display Name: Home Keygen Cookie
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HomeTestKeygenCookie"])
        )

    @property
    def CareOfTestNonceIndex(self):
        """
        Display Name: Care-of nonce index
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CareOfTestNonceIndex"])
        )

    @property
    def CareOfTestInitCookie(self):
        """
        Display Name: Care-of Init Cookie
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CareOfTestInitCookie"])
        )

    @property
    def CareOfTestKeygenCookie(self):
        """
        Display Name: Care-of Keygen Cookie
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CareOfTestKeygenCookie"])
        )

    @property
    def BindingUpdateSequence(self):
        """
        Display Name: Sequence Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BindingUpdateSequence"])
        )

    @property
    def BindingUpdateABit(self):
        """
        Display Name: A bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BindingUpdateABit"])
        )

    @property
    def BindingUpdateHBit(self):
        """
        Display Name: H bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BindingUpdateHBit"])
        )

    @property
    def BindingUpdateLBit(self):
        """
        Display Name: L bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BindingUpdateLBit"])
        )

    @property
    def BindingUpdateKBit(self):
        """
        Display Name: K bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BindingUpdateKBit"])
        )

    @property
    def BindingUpdateReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BindingUpdateReserved"])
        )

    @property
    def BindingUpdateLifetime(self):
        """
        Display Name: Lifetime
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BindingUpdateLifetime"])
        )

    @property
    def BindingAckStatus(self):
        """
        Display Name: Status
        Default Value: 0
        Value Format: decimal
        Available enum values: Binding Update accepted, 0, Accepted but prefix discovery necessary, 1, Reason unspecified, 128, Administratively prohibited, 129, Insufficient resources, 130, Home registration not supported, 131, Not home subnet, 132, Not home agent for this mobile node, 133, Duplicate Address Detection failed, 134, Sequence number out of window, 135, Expired home nonce index, 136, Expired care-of nonce index, 137, Expired nonces, 138, Registration type change disallowed, 139
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BindingAckStatus"])
        )

    @property
    def BindingAckKBit(self):
        """
        Display Name: K bit
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BindingAckKBit"])
        )

    @property
    def BindingAckReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BindingAckReserved"])
        )

    @property
    def BindingAckSequence(self):
        """
        Display Name: Sequence Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BindingAckSequence"])
        )

    @property
    def BindingAckLifetime(self):
        """
        Display Name: Lifetime
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BindingAckLifetime"])
        )

    @property
    def BindingErrorStatus(self):
        """
        Display Name: Status
        Default Value: 1
        Value Format: decimal
        Available enum values: Unknown binding for Home Address destination option, 1, Unrecognized MH Type value, 2
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BindingErrorStatus"])
        )

    @property
    def BindingErrorReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BindingErrorReserved"])
        )

    @property
    def BindingErrorHomeAddress(self):
        """
        Display Name: Home Address
        Default Value: 0::1
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BindingErrorHomeAddress"])
        )

    @property
    def Pad1Type(self):
        """
        Display Name: Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Pad1Type"]))

    @property
    def PadNType(self):
        """
        Display Name: Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PadNType"]))

    @property
    def PadNLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PadNLength"]))

    @property
    def PadNData(self):
        """
        Display Name: Data
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PadNData"]))

    @property
    def BindingRefreshAdviceType(self):
        """
        Display Name: Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BindingRefreshAdviceType"])
        )

    @property
    def BindingRefreshAdviceLength(self):
        """
        Display Name: Length
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BindingRefreshAdviceLength"])
        )

    @property
    def BindingRefreshAdviceData(self):
        """
        Display Name: Refresh Interval
        Default Value: 10
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BindingRefreshAdviceData"])
        )

    @property
    def AlternateCareOfAddressType(self):
        """
        Display Name: Type
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AlternateCareOfAddressType"])
        )

    @property
    def AlternateCareOfAddressLength(self):
        """
        Display Name: Length
        Default Value: 16
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AlternateCareOfAddressLength"])
        )

    @property
    def AlternateCareOfAddressData(self):
        """
        Display Name: Alternate Care-of Address
        Default Value: 0::1
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AlternateCareOfAddressData"])
        )

    @property
    def NonceIndicesType(self):
        """
        Display Name: Type
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NonceIndicesType"])
        )

    @property
    def NonceIndicesLength(self):
        """
        Display Name: Length
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NonceIndicesLength"])
        )

    @property
    def NonceIndicesHomeNonce(self):
        """
        Display Name: Home Nonce Index
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NonceIndicesHomeNonce"])
        )

    @property
    def NonceIndicesCareOfNonce(self):
        """
        Display Name: Care-of Nonce Index
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NonceIndicesCareOfNonce"])
        )

    @property
    def BindingAuthorizationDataType(self):
        """
        Display Name: Type
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BindingAuthorizationDataType"])
        )

    @property
    def BindingAuthorizationDataLength(self):
        """
        Display Name: Length
        Default Value: 12
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["BindingAuthorizationDataLength"]),
        )

    @property
    def BindingAuthorizationDataAuthenticator(self):
        """
        Display Name: Authenticator
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["BindingAuthorizationDataAuthenticator"]
            ),
        )

    @property
    def OptionsHolderPad(self):
        """
        Display Name: Padding
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["OptionsHolderPad"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
