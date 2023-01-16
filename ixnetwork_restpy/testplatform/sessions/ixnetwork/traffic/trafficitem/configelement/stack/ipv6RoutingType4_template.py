from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ipv6RoutingType4(Base):
    __slots__ = ()
    _SDM_NAME = "ipv6RoutingType4"
    _SDM_ATT_MAP = {
        "SegmentRoutingHeaderNextHeader": "ipv6RoutingType4.segmentRoutingHeader.nextHeader-1",
        "SegmentRoutingHeaderHdrExtLen": "ipv6RoutingType4.segmentRoutingHeader.hdrExtLen-2",
        "SegmentRoutingHeaderRoutingType": "ipv6RoutingType4.segmentRoutingHeader.routingType-3",
        "SegmentRoutingHeaderSegmentsLeft": "ipv6RoutingType4.segmentRoutingHeader.segmentsLeft-4",
        "SegmentRoutingHeaderLastEntry": "ipv6RoutingType4.segmentRoutingHeader.lastEntry-5",
        "FlagsU1Flag": "ipv6RoutingType4.segmentRoutingHeader.flags.u1Flag-6",
        "FlagsPFlag": "ipv6RoutingType4.segmentRoutingHeader.flags.pFlag-7",
        "FlagsOFlag": "ipv6RoutingType4.segmentRoutingHeader.flags.oFlag-8",
        "FlagsAFlag": "ipv6RoutingType4.segmentRoutingHeader.flags.aFlag-9",
        "FlagsHFlag": "ipv6RoutingType4.segmentRoutingHeader.flags.hFlag-10",
        "FlagsU2Flag": "ipv6RoutingType4.segmentRoutingHeader.flags.u2Flag-11",
        "SegmentRoutingHeaderTag": "ipv6RoutingType4.segmentRoutingHeader.tag-12",
        "SegmentListIpv6SID1": "ipv6RoutingType4.segmentRoutingHeader.segmentList.ipv6SID1-13",
        "SegmentListIpv6SID2": "ipv6RoutingType4.segmentRoutingHeader.segmentList.ipv6SID2-14",
        "SegmentListIpv6SID3": "ipv6RoutingType4.segmentRoutingHeader.segmentList.ipv6SID3-15",
        "SegmentListIpv6SID4": "ipv6RoutingType4.segmentRoutingHeader.segmentList.ipv6SID4-16",
        "SegmentListIpv6SID5": "ipv6RoutingType4.segmentRoutingHeader.segmentList.ipv6SID5-17",
        "SegmentListIpv6SID6": "ipv6RoutingType4.segmentRoutingHeader.segmentList.ipv6SID6-18",
        "SegmentListIpv6SID7": "ipv6RoutingType4.segmentRoutingHeader.segmentList.ipv6SID7-19",
        "SegmentListIpv6SID8": "ipv6RoutingType4.segmentRoutingHeader.segmentList.ipv6SID8-20",
        "SegmentListIpv6SID9": "ipv6RoutingType4.segmentRoutingHeader.segmentList.ipv6SID9-21",
        "SegmentListIpv6SID10": "ipv6RoutingType4.segmentRoutingHeader.segmentList.ipv6SID10-22",
        "SegmentListIpv6SID11": "ipv6RoutingType4.segmentRoutingHeader.segmentList.ipv6SID11-23",
        "SegmentListIpv6SID12": "ipv6RoutingType4.segmentRoutingHeader.segmentList.ipv6SID12-24",
        "SegmentListIpv6SID13": "ipv6RoutingType4.segmentRoutingHeader.segmentList.ipv6SID13-25",
        "SegmentListIpv6SID14": "ipv6RoutingType4.segmentRoutingHeader.segmentList.ipv6SID14-26",
        "SegmentListIpv6SID15": "ipv6RoutingType4.segmentRoutingHeader.segmentList.ipv6SID15-27",
        "SegmentListIpv6SID16": "ipv6RoutingType4.segmentRoutingHeader.segmentList.ipv6SID16-28",
        "SegmentListIpv6SID17": "ipv6RoutingType4.segmentRoutingHeader.segmentList.ipv6SID17-29",
        "SegmentListIpv6SID18": "ipv6RoutingType4.segmentRoutingHeader.segmentList.ipv6SID18-30",
        "SegmentListIpv6SID19": "ipv6RoutingType4.segmentRoutingHeader.segmentList.ipv6SID19-31",
        "SegmentListIpv6SID20": "ipv6RoutingType4.segmentRoutingHeader.segmentList.ipv6SID20-32",
        "Sripv6IngressNodeTLVTclType": "ipv6RoutingType4.segmentRoutingHeader.srhTLVs.sripv6IngressNodeTLV.tclType-33",
        "Sripv6IngressNodeTLVTclLength": "ipv6RoutingType4.segmentRoutingHeader.srhTLVs.sripv6IngressNodeTLV.tclLength-34",
        "Sripv6IngressNodeTLVTclReserved": "ipv6RoutingType4.segmentRoutingHeader.srhTLVs.sripv6IngressNodeTLV.tclReserved-35",
        "Sripv6IngressNodeTLVTclFlags": "ipv6RoutingType4.segmentRoutingHeader.srhTLVs.sripv6IngressNodeTLV.tclFlags-36",
        "Sripv6IngressNodeTLVTclValue": "ipv6RoutingType4.segmentRoutingHeader.srhTLVs.sripv6IngressNodeTLV.tclValue-37",
        "Sripv6EgressNodeTLVTclType": "ipv6RoutingType4.segmentRoutingHeader.srhTLVs.sripv6EgressNodeTLV.tclType-38",
        "Sripv6EgressNodeTLVTclLength": "ipv6RoutingType4.segmentRoutingHeader.srhTLVs.sripv6EgressNodeTLV.tclLength-39",
        "Sripv6EgressNodeTLVTclReserved": "ipv6RoutingType4.segmentRoutingHeader.srhTLVs.sripv6EgressNodeTLV.tclReserved-40",
        "Sripv6EgressNodeTLVTclFlags": "ipv6RoutingType4.segmentRoutingHeader.srhTLVs.sripv6EgressNodeTLV.tclFlags-41",
        "Sripv6EgressNodeTLVTclValue": "ipv6RoutingType4.segmentRoutingHeader.srhTLVs.sripv6EgressNodeTLV.tclValue-42",
        "Sripv6OpaqueContainerTLVTclType": "ipv6RoutingType4.segmentRoutingHeader.srhTLVs.sripv6OpaqueContainerTLV.tclType-43",
        "Sripv6OpaqueContainerTLVTclLength": "ipv6RoutingType4.segmentRoutingHeader.srhTLVs.sripv6OpaqueContainerTLV.tclLength-44",
        "Sripv6OpaqueContainerTLVTclReserved": "ipv6RoutingType4.segmentRoutingHeader.srhTLVs.sripv6OpaqueContainerTLV.tclReserved-45",
        "Sripv6OpaqueContainerTLVTclFlags": "ipv6RoutingType4.segmentRoutingHeader.srhTLVs.sripv6OpaqueContainerTLV.tclFlags-46",
        "Sripv6OpaqueContainerTLVTclValue": "ipv6RoutingType4.segmentRoutingHeader.srhTLVs.sripv6OpaqueContainerTLV.tclValue-47",
        "PathTraceTLVTclType": "ipv6RoutingType4.segmentRoutingHeader.srhTLVs.pathTraceTLV.tclType-48",
        "PathTraceTLVTclLength": "ipv6RoutingType4.segmentRoutingHeader.srhTLVs.pathTraceTLV.tclLength-49",
        "PathTraceTLVIfId": "ipv6RoutingType4.segmentRoutingHeader.srhTLVs.pathTraceTLV.ifId-50",
        "PathTraceTLVIfLd": "ipv6RoutingType4.segmentRoutingHeader.srhTLVs.pathTraceTLV.ifLd-51",
        "PathTraceTLVTimeStamp": "ipv6RoutingType4.segmentRoutingHeader.srhTLVs.pathTraceTLV.timeStamp-52",
        "PathTraceTLVSessionId": "ipv6RoutingType4.segmentRoutingHeader.srhTLVs.pathTraceTLV.sessionId-53",
        "PathTraceTLVSequenceNo": "ipv6RoutingType4.segmentRoutingHeader.srhTLVs.pathTraceTLV.sequenceNo-54",
        "Sripv6PaddingTLVTclType": "ipv6RoutingType4.segmentRoutingHeader.srhTLVs.sripv6PaddingTLV.tclType-55",
        "Sripv6PaddingTLVTclLength": "ipv6RoutingType4.segmentRoutingHeader.srhTLVs.sripv6PaddingTLV.tclLength-56",
        "Sripv6PaddingTLVPad": "ipv6RoutingType4.segmentRoutingHeader.srhTLVs.sripv6PaddingTLV.pad-57",
    }

    def __init__(self, parent, list_op=False):
        super(Ipv6RoutingType4, self).__init__(parent, list_op)

    @property
    def SegmentRoutingHeaderNextHeader(self):
        """
        Display Name: Next Header
        Default Value: 59
        Value Format: decimal
        Available enum values: HOPOPT, 0, ICMP, 1, IGMP, 2, GGP, 3, IP, 4, ST, 5, TCP, 6, CBT, 7, EGP, 8, IGP, 9, BBN-RCC-MON, 10, NVP-II, 11, PUP, 12, ARGUS, 13, EMCON, 14, XNET, 15, CHAOS, 16, UDP, 17, MUX, 18, DCN-MEAS, 19, HMP, 20, PRM, 21, XNS-IDP, 22, TRUNK-1, 23, TRUNK-2, 24, LEAF-1, 25, LEAF-2, 26, RDP, 27, IRTP, 28, ISO-TP4, 29, NETBLT, 30, MFE-NSP, 31, MERIT-INP, 32, SEP, 33, 3PC, 34, IDPR, 35, XTP, 36, DDP, 37, IDPR-CMTP, 38, TP++, 39, IL, 40, IPv6, 41, SDRP, 42, IPv6-Route, 43, IPv6-Frag, 44, IDRP, 45, RSVP, 46, GRE, 47, MHRP, 48, BNA, 49, ESP, 50, AH, 51, I-NLSP, 52, SWIPE, 53, NARP, 54, MOBILE, 55, TLSP, 56, SKIP, 57, IPv6-ICMP, 58, IPv6-NoNxt, 59, IPv6-Opts, 60, Any host internal protocol, 61, CFTP, 62, Any local network, 63, SAT-EXPAK, 64, KRYPTOLAN, 65, RVD, 66, IPPC, 67, Any distributed file system, 68, SAT-MON, 69, VISA, 70, IPCV, 71, CPNX, 72, CPHB, 73, WSN, 74, PVP, 75, BR-SAT-MON, 76, SUN-ND, 77, WB-MON, 78, WB-EXPAK, 79, ISO-IP, 80, VMTP, 81, SECURE-VMTP, 82, VINES, 83, TTP, 84, NSFNET-IGP, 85, DGP, 86, TCF, 87, EIGRP, 88, OSPFIGP, 89, Sprite-RPC, 90, LARP, 91, MTP, 92, AX.25, 93, IPIP, 94, MICP, 95, SCC-SP, 96, ETHERIP, 97, ENCAP, 98, Any private encryption, 99, GMTP, 100, IFMP, 101, PNNI, 102, PIM, 103, ARIS, 104, SCPS, 105, QNX, 106, A/N, 107, IPComp, 108, SNP, 109, Compaq-Peer, 110, IPX-in-IP, 111, VRRP, 112, PGM, 113, Any 0-hop protocol, 114, L2TP, 115, DDX, 116, IATP, 117, STP, 118, SRP, 119, UTI, 120, SMP, 121, SM, 122, PTP, 123, ISIS over IPv4, 124, FIRE, 125, CRTP, 126, CRUDP, 127, SSCOPMCE, 128, IPLT, 129, SPS, 130, PIPE, 131, SCTP, 132, FC, 133, RSVP-E2E-IGNORE, 134, Mobility Header, 135, UDPLite, 136, MPLS-in-IP, 137, Unassigned, 138, Unassigned, 139, Unassigned, 140, Unassigned, 141, Unassigned, 142, Unassigned, 143, Unassigned, 144, Unassigned, 145, Unassigned, 146, Unassigned, 147, Unassigned, 148, Unassigned, 149, Unassigned, 150, Unassigned, 151, Unassigned, 152, Unassigned, 153, Unassigned, 154, Unassigned, 155, Unassigned, 156, Unassigned, 157, Unassigned, 158, Unassigned, 159, Unassigned, 160, Unassigned, 161, Unassigned, 162, Unassigned, 163, Unassigned, 164, Unassigned, 165, Unassigned, 166, Unassigned, 167, Unassigned, 168, Unassigned, 169, Unassigned, 170, Unassigned, 171, Unassigned, 172, Unassigned, 173, Unassigned, 174, Unassigned, 175, Unassigned, 176, Unassigned, 177, Unassigned, 178, Unassigned, 179, Unassigned, 180, Unassigned, 181, Unassigned, 182, Unassigned, 183, Unassigned, 184, Unassigned, 185, Unassigned, 186, Unassigned, 187, Unassigned, 188, Unassigned, 189, Unassigned, 190, Unassigned, 191, Unassigned, 192, Unassigned, 193, Unassigned, 194, Unassigned, 195, Unassigned, 196, Unassigned, 197, Unassigned, 198, Unassigned, 199, Unassigned, 200, Unassigned, 201, Unassigned, 202, Unassigned, 203, Unassigned, 204, Unassigned, 205, Unassigned, 206, Unassigned, 207, Unassigned, 208, Unassigned, 209, Unassigned, 210, Unassigned, 211, Unassigned, 212, Unassigned, 213, Unassigned, 214, Unassigned, 215, Unassigned, 216, Unassigned, 217, Unassigned, 218, Unassigned, 219, Unassigned, 220, Unassigned, 221, Unassigned, 222, Unassigned, 223, Unassigned, 224, Unassigned, 225, Unassigned, 226, Unassigned, 227, Unassigned, 228, Unassigned, 229, Unassigned, 230, Unassigned, 231, Unassigned, 232, Unassigned, 233, Unassigned, 234, Unassigned, 235, Unassigned, 236, Unassigned, 237, Unassigned, 238, Unassigned, 239, Unassigned, 240, Unassigned, 241, Unassigned, 242, Unassigned, 243, Unassigned, 244, Unassigned, 245, Unassigned, 246, Unassigned, 247, Unassigned, 248, Unassigned, 249, Unassigned, 250, Unassigned, 251, Unassigned, 252, Unassigned, 253, Unassigned, 254, Reserved, 255
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SegmentRoutingHeaderNextHeader"]),
        )

    @property
    def SegmentRoutingHeaderHdrExtLen(self):
        """
        Display Name: Hdr Ext Len
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SegmentRoutingHeaderHdrExtLen"]),
        )

    @property
    def SegmentRoutingHeaderRoutingType(self):
        """
        Display Name: Routing Type
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SegmentRoutingHeaderRoutingType"]),
        )

    @property
    def SegmentRoutingHeaderSegmentsLeft(self):
        """
        Display Name: Segments Left
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SegmentRoutingHeaderSegmentsLeft"]),
        )

    @property
    def SegmentRoutingHeaderLastEntry(self):
        """
        Display Name: Last Entry
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SegmentRoutingHeaderLastEntry"]),
        )

    @property
    def FlagsU1Flag(self):
        """
        Display Name: U1
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FlagsU1Flag"]))

    @property
    def FlagsPFlag(self):
        """
        Display Name: P
        Default Value: 0
        Value Format: decimal
        Available enum values: Not Protected through FRR, 0, Protected through FRR, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FlagsPFlag"]))

    @property
    def FlagsOFlag(self):
        """
        Display Name: O
        Default Value: 0
        Value Format: decimal
        Available enum values: Not OAM Packet, 0, OAM Packet, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FlagsOFlag"]))

    @property
    def FlagsAFlag(self):
        """
        Display Name: A
        Default Value: 0
        Value Format: decimal
        Available enum values: No Alert (important TLVs not present), 0, Important TLVs are Present, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FlagsAFlag"]))

    @property
    def FlagsHFlag(self):
        """
        Display Name: H
        Default Value: 0
        Value Format: decimal
        Available enum values: No HMAC TLV, 0, HMAC TLV present, 1
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FlagsHFlag"]))

    @property
    def FlagsU2Flag(self):
        """
        Display Name: U2
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FlagsU2Flag"]))

    @property
    def SegmentRoutingHeaderTag(self):
        """
        Display Name: Tag
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SegmentRoutingHeaderTag"])
        )

    @property
    def SegmentListIpv6SID1(self):
        """
        Display Name: IPv6 SID 0
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SegmentListIpv6SID1"])
        )

    @property
    def SegmentListIpv6SID2(self):
        """
        Display Name: IPv6 SID 1
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SegmentListIpv6SID2"])
        )

    @property
    def SegmentListIpv6SID3(self):
        """
        Display Name: IPv6 SID 2
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SegmentListIpv6SID3"])
        )

    @property
    def SegmentListIpv6SID4(self):
        """
        Display Name: IPv6 SID 3
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SegmentListIpv6SID4"])
        )

    @property
    def SegmentListIpv6SID5(self):
        """
        Display Name: IPv6 SID 4
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SegmentListIpv6SID5"])
        )

    @property
    def SegmentListIpv6SID6(self):
        """
        Display Name: IPv6 SID 5
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SegmentListIpv6SID6"])
        )

    @property
    def SegmentListIpv6SID7(self):
        """
        Display Name: IPv6 SID 6
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SegmentListIpv6SID7"])
        )

    @property
    def SegmentListIpv6SID8(self):
        """
        Display Name: IPv6 SID 7
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SegmentListIpv6SID8"])
        )

    @property
    def SegmentListIpv6SID9(self):
        """
        Display Name: IPv6 SID 8
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SegmentListIpv6SID9"])
        )

    @property
    def SegmentListIpv6SID10(self):
        """
        Display Name: IPv6 SID 9
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SegmentListIpv6SID10"])
        )

    @property
    def SegmentListIpv6SID11(self):
        """
        Display Name: IPv6 SID 10
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SegmentListIpv6SID11"])
        )

    @property
    def SegmentListIpv6SID12(self):
        """
        Display Name: IPv6 SID 11
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SegmentListIpv6SID12"])
        )

    @property
    def SegmentListIpv6SID13(self):
        """
        Display Name: IPv6 SID 12
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SegmentListIpv6SID13"])
        )

    @property
    def SegmentListIpv6SID14(self):
        """
        Display Name: IPv6 SID 13
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SegmentListIpv6SID14"])
        )

    @property
    def SegmentListIpv6SID15(self):
        """
        Display Name: IPv6 SID 14
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SegmentListIpv6SID15"])
        )

    @property
    def SegmentListIpv6SID16(self):
        """
        Display Name: IPv6 SID 15
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SegmentListIpv6SID16"])
        )

    @property
    def SegmentListIpv6SID17(self):
        """
        Display Name: IPv6 SID 16
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SegmentListIpv6SID17"])
        )

    @property
    def SegmentListIpv6SID18(self):
        """
        Display Name: IPv6 SID 17
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SegmentListIpv6SID18"])
        )

    @property
    def SegmentListIpv6SID19(self):
        """
        Display Name: IPv6 SID 18
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SegmentListIpv6SID19"])
        )

    @property
    def SegmentListIpv6SID20(self):
        """
        Display Name: IPv6 SID 19
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["SegmentListIpv6SID20"])
        )

    @property
    def Sripv6IngressNodeTLVTclType(self):
        """
        Display Name: Type
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Sripv6IngressNodeTLVTclType"])
        )

    @property
    def Sripv6IngressNodeTLVTclLength(self):
        """
        Display Name: Length
        Default Value: 18
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Sripv6IngressNodeTLVTclLength"]),
        )

    @property
    def Sripv6IngressNodeTLVTclReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Sripv6IngressNodeTLVTclReserved"]),
        )

    @property
    def Sripv6IngressNodeTLVTclFlags(self):
        """
        Display Name: Flags
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Sripv6IngressNodeTLVTclFlags"])
        )

    @property
    def Sripv6IngressNodeTLVTclValue(self):
        """
        Display Name: Value
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Sripv6IngressNodeTLVTclValue"])
        )

    @property
    def Sripv6EgressNodeTLVTclType(self):
        """
        Display Name: Type
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Sripv6EgressNodeTLVTclType"])
        )

    @property
    def Sripv6EgressNodeTLVTclLength(self):
        """
        Display Name: Length
        Default Value: 18
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Sripv6EgressNodeTLVTclLength"])
        )

    @property
    def Sripv6EgressNodeTLVTclReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Sripv6EgressNodeTLVTclReserved"]),
        )

    @property
    def Sripv6EgressNodeTLVTclFlags(self):
        """
        Display Name: Flags
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Sripv6EgressNodeTLVTclFlags"])
        )

    @property
    def Sripv6EgressNodeTLVTclValue(self):
        """
        Display Name: Value
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Sripv6EgressNodeTLVTclValue"])
        )

    @property
    def Sripv6OpaqueContainerTLVTclType(self):
        """
        Display Name: Type
        Default Value: 3
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Sripv6OpaqueContainerTLVTclType"]),
        )

    @property
    def Sripv6OpaqueContainerTLVTclLength(self):
        """
        Display Name: Length
        Default Value: 18
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Sripv6OpaqueContainerTLVTclLength"]),
        )

    @property
    def Sripv6OpaqueContainerTLVTclReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Sripv6OpaqueContainerTLVTclReserved"]
            ),
        )

    @property
    def Sripv6OpaqueContainerTLVTclFlags(self):
        """
        Display Name: Flags
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Sripv6OpaqueContainerTLVTclFlags"]),
        )

    @property
    def Sripv6OpaqueContainerTLVTclValue(self):
        """
        Display Name: Value
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Sripv6OpaqueContainerTLVTclValue"]),
        )

    @property
    def PathTraceTLVTclType(self):
        """
        Display Name: Type
        Default Value: 128
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PathTraceTLVTclType"])
        )

    @property
    def PathTraceTLVTclLength(self):
        """
        Display Name: Length
        Default Value: 14
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PathTraceTLVTclLength"])
        )

    @property
    def PathTraceTLVIfId(self):
        """
        Display Name: Interface ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PathTraceTLVIfId"])
        )

    @property
    def PathTraceTLVIfLd(self):
        """
        Display Name: Interface Load
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PathTraceTLVIfLd"])
        )

    @property
    def PathTraceTLVTimeStamp(self):
        """
        Display Name: Timestamp
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PathTraceTLVTimeStamp"])
        )

    @property
    def PathTraceTLVSessionId(self):
        """
        Display Name: Session ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PathTraceTLVSessionId"])
        )

    @property
    def PathTraceTLVSequenceNo(self):
        """
        Display Name: Sequence Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PathTraceTLVSequenceNo"])
        )

    @property
    def Sripv6PaddingTLVTclType(self):
        """
        Display Name: Type
        Default Value: 4
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Sripv6PaddingTLVTclType"])
        )

    @property
    def Sripv6PaddingTLVTclLength(self):
        """
        Display Name: Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Sripv6PaddingTLVTclLength"])
        )

    @property
    def Sripv6PaddingTLVPad(self):
        """
        Display Name: Padding
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Sripv6PaddingTLVPad"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
