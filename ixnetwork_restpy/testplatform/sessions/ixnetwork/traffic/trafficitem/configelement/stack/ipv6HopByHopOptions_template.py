from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ipv6HopByHopOptions(Base):
    __slots__ = ()
    _SDM_NAME = "ipv6HopByHopOptions"
    _SDM_ATT_MAP = {
        "HopByHopOptionsHeaderNextHeader": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.nextHeader-1",
        "HopByHopOptionsHeaderHeaderExtensionLength": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.headerExtensionLength-2",
        "TypeUnrecognizedType": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.userDefined.type.unrecognizedType-3",
        "TypeAllowPacketChange": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.userDefined.type.allowPacketChange-4",
        "TypeUserDefinedType": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.userDefined.type.userDefinedType-5",
        "UserDefinedLength": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.userDefined.length-6",
        "UserDefinedData": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.userDefined.data-7",
        "PadNType": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.padN.type-8",
        "PadNLength": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.padN.length-9",
        "PadNData": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.padN.data-10",
        "OptionPad1": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pad1-11",
        "PathTracingType": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.type-12",
        "PathTracingLength": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.length-13",
        "Mcd1OifId": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd1.oifId-14",
        "Mcd1Oil": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd1.oil-15",
        "Mcd1Tts": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd1.tts-16",
        "Mcd2OifId": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd2.oifId-17",
        "Mcd2Oil": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd2.oil-18",
        "Mcd2Tts": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd2.tts-19",
        "Mcd3OifId": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd3.oifId-20",
        "Mcd3Oil": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd3.oil-21",
        "Mcd3Tts": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd3.tts-22",
        "Mcd4OifId": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd4.oifId-23",
        "Mcd4Oil": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd4.oil-24",
        "Mcd4Tts": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd4.tts-25",
        "Mcd5OifId": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd5.oifId-26",
        "Mcd5Oil": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd5.oil-27",
        "Mcd5Tts": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd5.tts-28",
        "Mcd6OifId": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd6.oifId-29",
        "Mcd6Oil": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd6.oil-30",
        "Mcd6Tts": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd6.tts-31",
        "Mcd7OifId": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd7.oifId-32",
        "Mcd7Oil": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd7.oil-33",
        "Mcd7Tts": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd7.tts-34",
        "Mcd8OifId": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd8.oifId-35",
        "Mcd8Oil": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd8.oil-36",
        "Mcd8Tts": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd8.tts-37",
        "Mcd9OifId": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd9.oifId-38",
        "Mcd9Oil": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd9.oil-39",
        "Mcd9Tts": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd9.tts-40",
        "Mcd10OifId": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd10.oifId-41",
        "Mcd10Oil": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd10.oil-42",
        "Mcd10Tts": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd10.tts-43",
        "Mcd11OifId": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd11.oifId-44",
        "Mcd11Oil": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd11.oil-45",
        "Mcd11Tts": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd11.tts-46",
        "Mcd12OifId": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd12.oifId-47",
        "Mcd12Oil": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd12.oil-48",
        "Mcd12Tts": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd12.tts-49",
        "Mcd13OifId": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd13.oifId-50",
        "Mcd13Oil": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd13.oil-51",
        "Mcd13Tts": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd13.tts-52",
        "Mcd14OifId": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd14.oifId-53",
        "Mcd14Oil": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd14.oil-54",
        "Mcd14Tts": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd14.tts-55",
        "Mcd15OifId": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd15.oifId-56",
        "Mcd15Oil": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd15.oil-57",
        "Mcd15Tts": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd15.tts-58",
        "Mcd16OifId": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd16.oifId-59",
        "Mcd16Oil": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd16.oil-60",
        "Mcd16Tts": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd16.tts-61",
        "Mcd17OifId": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd17.oifId-62",
        "Mcd17Oil": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd17.oil-63",
        "Mcd17Tts": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd17.tts-64",
        "Mcd18OifId": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd18.oifId-65",
        "Mcd18Oil": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd18.oil-66",
        "Mcd18Tts": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd18.tts-67",
        "Mcd19OifId": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd19.oifId-68",
        "Mcd19Oil": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd19.oil-69",
        "Mcd19Tts": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd19.tts-70",
        "Mcd20OifId": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd20.oifId-71",
        "Mcd20Oil": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd20.oil-72",
        "Mcd20Tts": "ipv6HopByHopOptions.header.hopByHopOptionsHeader.options.option.pathTracing.data.mcd20.tts-73",
        "HeaderPad": "ipv6HopByHopOptions.header.pad-74",
    }

    def __init__(self, parent, list_op=False):
        super(Ipv6HopByHopOptions, self).__init__(parent, list_op)

    @property
    def HopByHopOptionsHeaderNextHeader(self):
        """
        Display Name: Next Header
        Default Value: 59
        Value Format: decimal
        Available enum values: HOPOPT, 0, ICMP, 1, IGMP, 2, GGP, 3, IP, 4, ST, 5, TCP, 6, CBT, 7, EGP, 8, IGP, 9, BBN-RCC-MON, 10, NVP-II, 11, PUP, 12, ARGUS, 13, EMCON, 14, XNET, 15, CHAOS, 16, UDP, 17, MUX, 18, DCN-MEAS, 19, HMP, 20, PRM, 21, XNS-IDP, 22, TRUNK-1, 23, TRUNK-2, 24, LEAF-1, 25, LEAF-2, 26, RDP, 27, IRTP, 28, ISO-TP4, 29, NETBLT, 30, MFE-NSP, 31, MERIT-INP, 32, SEP, 33, 3PC, 34, IDPR, 35, XTP, 36, DDP, 37, IDPR-CMTP, 38, TP++, 39, IL, 40, IPv6, 41, SDRP, 42, IPv6-Route, 43, IPv6-Frag, 44, IDRP, 45, RSVP, 46, GRE, 47, MHRP, 48, BNA, 49, ESP, 50, AH, 51, I-NLSP, 52, SWIPE, 53, NARP, 54, MOBILE, 55, TLSP, 56, SKIP, 57, IPv6-ICMP, 58, IPv6-NoNxt, 59, IPv6-Opts, 60, Any host internal protocol, 61, CFTP, 62, Any local network, 63, SAT-EXPAK, 64, KRYPTOLAN, 65, RVD, 66, IPPC, 67, Any distributed file system, 68, SAT-MON, 69, VISA, 70, IPCV, 71, CPNX, 72, CPHB, 73, WSN, 74, PVP, 75, BR-SAT-MON, 76, SUN-ND, 77, WB-MON, 78, WB-EXPAK, 79, ISO-IP, 80, VMTP, 81, SECURE-VMTP, 82, VINES, 83, TTP, 84, NSFNET-IGP, 85, DGP, 86, TCF, 87, EIGRP, 88, OSPFIGP, 89, Sprite-RPC, 90, LARP, 91, MTP, 92, AX.25, 93, IPIP, 94, MICP, 95, SCC-SP, 96, ETHERIP, 97, ENCAP, 98, Any private encryption, 99, GMTP, 100, IFMP, 101, PNNI, 102, PIM, 103, ARIS, 104, SCPS, 105, QNX, 106, A/N, 107, IPComp, 108, SNP, 109, Compaq-Peer, 110, IPX-in-IP, 111, VRRP, 112, PGM, 113, Any 0-hop protocol, 114, L2TP, 115, DDX, 116, IATP, 117, STP, 118, SRP, 119, UTI, 120, SMP, 121, SM, 122, PTP, 123, ISIS over IPv4, 124, FIRE, 125, CRTP, 126, CRUDP, 127, SSCOPMCE, 128, IPLT, 129, SPS, 130, PIPE, 131, SCTP, 132, FC, 133, RSVP-E2E-IGNORE, 134, Mobility Header, 135, UDPLite, 136, MPLS-in-IP, 137, Unassigned, 138, Unassigned, 139, Unassigned, 140, Unassigned, 141, Unassigned, 142, Unassigned, 143, Unassigned, 144, Unassigned, 145, Unassigned, 146, Unassigned, 147, Unassigned, 148, Unassigned, 149, Unassigned, 150, Unassigned, 151, Unassigned, 152, Unassigned, 153, Unassigned, 154, Unassigned, 155, Unassigned, 156, Unassigned, 157, Unassigned, 158, Unassigned, 159, Unassigned, 160, Unassigned, 161, Unassigned, 162, Unassigned, 163, Unassigned, 164, Unassigned, 165, Unassigned, 166, Unassigned, 167, Unassigned, 168, Unassigned, 169, Unassigned, 170, Unassigned, 171, Unassigned, 172, Unassigned, 173, Unassigned, 174, Unassigned, 175, Unassigned, 176, Unassigned, 177, Unassigned, 178, Unassigned, 179, Unassigned, 180, Unassigned, 181, Unassigned, 182, Unassigned, 183, Unassigned, 184, Unassigned, 185, Unassigned, 186, Unassigned, 187, Unassigned, 188, Unassigned, 189, Unassigned, 190, Unassigned, 191, Unassigned, 192, Unassigned, 193, Unassigned, 194, Unassigned, 195, Unassigned, 196, Unassigned, 197, Unassigned, 198, Unassigned, 199, Unassigned, 200, Unassigned, 201, Unassigned, 202, Unassigned, 203, Unassigned, 204, Unassigned, 205, Unassigned, 206, Unassigned, 207, Unassigned, 208, Unassigned, 209, Unassigned, 210, Unassigned, 211, Unassigned, 212, Unassigned, 213, Unassigned, 214, Unassigned, 215, Unassigned, 216, Unassigned, 217, Unassigned, 218, Unassigned, 219, Unassigned, 220, Unassigned, 221, Unassigned, 222, Unassigned, 223, Unassigned, 224, Unassigned, 225, Unassigned, 226, Unassigned, 227, Unassigned, 228, Unassigned, 229, Unassigned, 230, Unassigned, 231, Unassigned, 232, Unassigned, 233, Unassigned, 234, Unassigned, 235, Unassigned, 236, Unassigned, 237, Unassigned, 238, Unassigned, 239, Unassigned, 240, Unassigned, 241, Unassigned, 242, Unassigned, 243, Unassigned, 244, Unassigned, 245, Unassigned, 246, Unassigned, 247, Unassigned, 248, Unassigned, 249, Unassigned, 250, Unassigned, 251, Unassigned, 252, Unassigned, 253, Unassigned, 254, Reserved, 255
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["HopByHopOptionsHeaderNextHeader"]),
        )

    @property
    def HopByHopOptionsHeaderHeaderExtensionLength(self):
        """
        Display Name: Header Extension Length (8 octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["HopByHopOptionsHeaderHeaderExtensionLength"]
            ),
        )

    @property
    def TypeUnrecognizedType(self):
        """
        Display Name: Option unrecognized
        Default Value: 0
        Value Format: decimal
        Available enum values: Skip and Continue Processing, 0, Discard Packet, 1, Discard Packet, Send ICMP with Code 2, 10, Discard Packet, Send ICMP with Code 2 if destination not multicast, 11
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TypeUnrecognizedType"])
        )

    @property
    def TypeAllowPacketChange(self):
        """
        Display Name: Allow Packet Change
        Default Value: 0
        Value Format: decimal
        Available enum values: Option Data cannot change en-route, 0, Option Data can change en-route, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TypeAllowPacketChange"])
        )

    @property
    def TypeUserDefinedType(self):
        """
        Display Name: User defined Option Type
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TypeUserDefinedType"])
        )

    @property
    def UserDefinedLength(self):
        """
        Display Name: Option length (octets)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UserDefinedLength"])
        )

    @property
    def UserDefinedData(self):
        """
        Display Name: Option Data
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["UserDefinedData"])
        )

    @property
    def PadNType(self):
        """
        Display Name: Option type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PadNType"]))

    @property
    def PadNLength(self):
        """
        Display Name: Option length (octets)
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PadNLength"]))

    @property
    def PadNData(self):
        """
        Display Name: Option Data
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PadNData"]))

    @property
    def OptionPad1(self):
        """
        Display Name: Pad1 Option
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["OptionPad1"]))

    @property
    def PathTracingType(self):
        """
        Display Name: Option type
        Default Value: 50
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PathTracingType"])
        )

    @property
    def PathTracingLength(self):
        """
        Display Name: Option length (octets)
        Default Value: 36
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PathTracingLength"])
        )

    @property
    def Mcd1OifId(self):
        """
        Display Name: Outgoing Interface ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd1OifId"]))

    @property
    def Mcd1Oil(self):
        """
        Display Name: Outgoing Interface Load
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd1Oil"]))

    @property
    def Mcd1Tts(self):
        """
        Display Name: Truncated Timestamp
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd1Tts"]))

    @property
    def Mcd2OifId(self):
        """
        Display Name: Outgoing Interface ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd2OifId"]))

    @property
    def Mcd2Oil(self):
        """
        Display Name: Outgoing Interface Load
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd2Oil"]))

    @property
    def Mcd2Tts(self):
        """
        Display Name: Truncated Timestamp
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd2Tts"]))

    @property
    def Mcd3OifId(self):
        """
        Display Name: Outgoing Interface ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd3OifId"]))

    @property
    def Mcd3Oil(self):
        """
        Display Name: Outgoing Interface Load
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd3Oil"]))

    @property
    def Mcd3Tts(self):
        """
        Display Name: Truncated Timestamp
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd3Tts"]))

    @property
    def Mcd4OifId(self):
        """
        Display Name: Outgoing Interface ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd4OifId"]))

    @property
    def Mcd4Oil(self):
        """
        Display Name: Outgoing Interface Load
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd4Oil"]))

    @property
    def Mcd4Tts(self):
        """
        Display Name: Truncated Timestamp
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd4Tts"]))

    @property
    def Mcd5OifId(self):
        """
        Display Name: Outgoing Interface ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd5OifId"]))

    @property
    def Mcd5Oil(self):
        """
        Display Name: Outgoing Interface Load
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd5Oil"]))

    @property
    def Mcd5Tts(self):
        """
        Display Name: Truncated Timestamp
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd5Tts"]))

    @property
    def Mcd6OifId(self):
        """
        Display Name: Outgoing Interface ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd6OifId"]))

    @property
    def Mcd6Oil(self):
        """
        Display Name: Outgoing Interface Load
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd6Oil"]))

    @property
    def Mcd6Tts(self):
        """
        Display Name: Truncated Timestamp
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd6Tts"]))

    @property
    def Mcd7OifId(self):
        """
        Display Name: Outgoing Interface ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd7OifId"]))

    @property
    def Mcd7Oil(self):
        """
        Display Name: Outgoing Interface Load
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd7Oil"]))

    @property
    def Mcd7Tts(self):
        """
        Display Name: Truncated Timestamp
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd7Tts"]))

    @property
    def Mcd8OifId(self):
        """
        Display Name: Outgoing Interface ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd8OifId"]))

    @property
    def Mcd8Oil(self):
        """
        Display Name: Outgoing Interface Load
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd8Oil"]))

    @property
    def Mcd8Tts(self):
        """
        Display Name: Truncated Timestamp
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd8Tts"]))

    @property
    def Mcd9OifId(self):
        """
        Display Name: Outgoing Interface ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd9OifId"]))

    @property
    def Mcd9Oil(self):
        """
        Display Name: Outgoing Interface Load
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd9Oil"]))

    @property
    def Mcd9Tts(self):
        """
        Display Name: Truncated Timestamp
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd9Tts"]))

    @property
    def Mcd10OifId(self):
        """
        Display Name: Outgoing Interface ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd10OifId"]))

    @property
    def Mcd10Oil(self):
        """
        Display Name: Outgoing Interface Load
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd10Oil"]))

    @property
    def Mcd10Tts(self):
        """
        Display Name: Truncated Timestamp
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd10Tts"]))

    @property
    def Mcd11OifId(self):
        """
        Display Name: Outgoing Interface ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd11OifId"]))

    @property
    def Mcd11Oil(self):
        """
        Display Name: Outgoing Interface Load
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd11Oil"]))

    @property
    def Mcd11Tts(self):
        """
        Display Name: Truncated Timestamp
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd11Tts"]))

    @property
    def Mcd12OifId(self):
        """
        Display Name: Outgoing Interface ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd12OifId"]))

    @property
    def Mcd12Oil(self):
        """
        Display Name: Outgoing Interface Load
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd12Oil"]))

    @property
    def Mcd12Tts(self):
        """
        Display Name: Truncated Timestamp
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd12Tts"]))

    @property
    def Mcd13OifId(self):
        """
        Display Name: Outgoing Interface ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd13OifId"]))

    @property
    def Mcd13Oil(self):
        """
        Display Name: Outgoing Interface Load
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd13Oil"]))

    @property
    def Mcd13Tts(self):
        """
        Display Name: Truncated Timestamp
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd13Tts"]))

    @property
    def Mcd14OifId(self):
        """
        Display Name: Outgoing Interface ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd14OifId"]))

    @property
    def Mcd14Oil(self):
        """
        Display Name: Outgoing Interface Load
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd14Oil"]))

    @property
    def Mcd14Tts(self):
        """
        Display Name: Truncated Timestamp
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd14Tts"]))

    @property
    def Mcd15OifId(self):
        """
        Display Name: Outgoing Interface ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd15OifId"]))

    @property
    def Mcd15Oil(self):
        """
        Display Name: Outgoing Interface Load
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd15Oil"]))

    @property
    def Mcd15Tts(self):
        """
        Display Name: Truncated Timestamp
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd15Tts"]))

    @property
    def Mcd16OifId(self):
        """
        Display Name: Outgoing Interface ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd16OifId"]))

    @property
    def Mcd16Oil(self):
        """
        Display Name: Outgoing Interface Load
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd16Oil"]))

    @property
    def Mcd16Tts(self):
        """
        Display Name: Truncated Timestamp
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd16Tts"]))

    @property
    def Mcd17OifId(self):
        """
        Display Name: Outgoing Interface ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd17OifId"]))

    @property
    def Mcd17Oil(self):
        """
        Display Name: Outgoing Interface Load
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd17Oil"]))

    @property
    def Mcd17Tts(self):
        """
        Display Name: Truncated Timestamp
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd17Tts"]))

    @property
    def Mcd18OifId(self):
        """
        Display Name: Outgoing Interface ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd18OifId"]))

    @property
    def Mcd18Oil(self):
        """
        Display Name: Outgoing Interface Load
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd18Oil"]))

    @property
    def Mcd18Tts(self):
        """
        Display Name: Truncated Timestamp
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd18Tts"]))

    @property
    def Mcd19OifId(self):
        """
        Display Name: Outgoing Interface ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd19OifId"]))

    @property
    def Mcd19Oil(self):
        """
        Display Name: Outgoing Interface Load
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd19Oil"]))

    @property
    def Mcd19Tts(self):
        """
        Display Name: Truncated Timestamp
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd19Tts"]))

    @property
    def Mcd20OifId(self):
        """
        Display Name: Outgoing Interface ID
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd20OifId"]))

    @property
    def Mcd20Oil(self):
        """
        Display Name: Outgoing Interface Load
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd20Oil"]))

    @property
    def Mcd20Tts(self):
        """
        Display Name: Truncated Timestamp
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Mcd20Tts"]))

    @property
    def HeaderPad(self):
        """
        Display Name: Padding
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderPad"]))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
