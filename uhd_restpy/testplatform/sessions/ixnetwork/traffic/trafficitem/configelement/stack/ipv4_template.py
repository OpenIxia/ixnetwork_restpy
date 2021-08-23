from uhd_restpy.base import Base
from uhd_restpy.files import Files


class Ipv4(Base):
    __slots__ = ()
    _SDM_NAME = 'ipv4'
    _SDM_ATT_MAP = {
        'Version': 'ipv4.header.version-1',
        'HeaderLength': 'ipv4.header.headerLength-2',
        'PriorityRaw': 'ipv4.header.priority.raw-3',
        'TosPrecedence': 'ipv4.header.priority.tos.precedence-4',
        'TosDelay': 'ipv4.header.priority.tos.delay-5',
        'TosThroughput': 'ipv4.header.priority.tos.throughput-6',
        'TosReliability': 'ipv4.header.priority.tos.reliability-7',
        'TosMonetary': 'ipv4.header.priority.tos.monetary-8',
        'TosUnused': 'ipv4.header.priority.tos.unused-9',
        'DefaultPHBDefaultPHB': 'ipv4.header.priority.ds.phb.defaultPHB.defaultPHB-10',
        'DefaultPHBUnused': 'ipv4.header.priority.ds.phb.defaultPHB.unused-11',
        'ClassSelectorPHBClassSelectorPHB': 'ipv4.header.priority.ds.phb.classSelectorPHB.classSelectorPHB-12',
        'ClassSelectorPHBUnused': 'ipv4.header.priority.ds.phb.classSelectorPHB.unused-13',
        'AssuredForwardingPHBAssuredForwardingPHB': 'ipv4.header.priority.ds.phb.assuredForwardingPHB.assuredForwardingPHB-14',
        'AssuredForwardingPHBUnused': 'ipv4.header.priority.ds.phb.assuredForwardingPHB.unused-15',
        'ExpeditedForwardingPHBExpeditedForwardingPHB': 'ipv4.header.priority.ds.phb.expeditedForwardingPHB.expeditedForwardingPHB-16',
        'ExpeditedForwardingPHBUnused': 'ipv4.header.priority.ds.phb.expeditedForwardingPHB.unused-17',
        'TotalLength': 'ipv4.header.totalLength-18',
        'Identification': 'ipv4.header.identification-19',
        'FlagsReserved': 'ipv4.header.flags.reserved-20',
        'FlagsFragment': 'ipv4.header.flags.fragment-21',
        'FlagsLastFragment': 'ipv4.header.flags.lastFragment-22',
        'FragmentOffset': 'ipv4.header.fragmentOffset-23',
        'Ttl': 'ipv4.header.ttl-24',
        'Protocol': 'ipv4.header.protocol-25',
        'Checksum': 'ipv4.header.checksum-26',
        'SrcIp': 'ipv4.header.srcIp-27',
        'DstIp': 'ipv4.header.dstIp-28',
        'OptionNop': 'ipv4.header.options.nextOption.option.nop-29',
        'SecurityType': 'ipv4.header.options.nextOption.option.security.type-30',
        'SecurityLength': 'ipv4.header.options.nextOption.option.security.length-31',
        'SecuritySecurity': 'ipv4.header.options.nextOption.option.security.security-32',
        'SecurityCompartments': 'ipv4.header.options.nextOption.option.security.compartments-33',
        'SecurityHandling': 'ipv4.header.options.nextOption.option.security.handling-34',
        'SecurityTcc': 'ipv4.header.options.nextOption.option.security.tcc-35',
        'LsrrType': 'ipv4.header.options.nextOption.option.lsrr.type-36',
        'LsrrLength': 'ipv4.header.options.nextOption.option.lsrr.length-37',
        'OptionPointer': 'ipv4.header.options.nextOption.option.pointer-38',
        'OptionRouteData': 'ipv4.header.options.nextOption.option.routeData-39',
        'SsrrType': 'ipv4.header.options.nextOption.option.ssrr.type-40',
        'SsrrLength': 'ipv4.header.options.nextOption.option.ssrr.length-41',
        'RecordRouteType': 'ipv4.header.options.nextOption.option.recordRoute.type-42',
        'RecordRouteLength': 'ipv4.header.options.nextOption.option.recordRoute.length-43',
        'StreamIdType': 'ipv4.header.options.nextOption.option.streamId.type-44',
        'StreamIdLength': 'ipv4.header.options.nextOption.option.streamId.length-45',
        'StreamIdId': 'ipv4.header.options.nextOption.option.streamId.id-46',
        'TimestampType': 'ipv4.header.options.nextOption.option.timestamp.type-47',
        'TimestampLength': 'ipv4.header.options.nextOption.option.timestamp.length-48',
        'TimestampPointer': 'ipv4.header.options.nextOption.option.timestamp.pointer-49',
        'TimestampOverflow': 'ipv4.header.options.nextOption.option.timestamp.overflow-50',
        'TimestampFlags': 'ipv4.header.options.nextOption.option.timestamp.flags-51',
        'PairAddress': 'ipv4.header.options.nextOption.option.timestamp.pair.address-52',
        'PairTimestamp': 'ipv4.header.options.nextOption.option.timestamp.pair.timestamp-53',
        'OptionLast': 'ipv4.header.options.nextOption.option.last-54',
        'RouterAlertType': 'ipv4.header.options.nextOption.option.routerAlert.type-55',
        'RouterAlertLength': 'ipv4.header.options.nextOption.option.routerAlert.length-56',
        'RouterAlertValue': 'ipv4.header.options.nextOption.option.routerAlert.value-57',
        'OptionsPad': 'ipv4.header.options.pad-58',
    }

    def __init__(self, parent, list_op=False):
        super(Ipv4, self).__init__(parent, list_op)

    @property
    def Version(self):
        """
        Display Name: Version
        Default Value: 4
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Version']))

    @property
    def HeaderLength(self):
        """
        Display Name: Header Length
        Default Value: 0
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['HeaderLength']))

    @property
    def PriorityRaw(self):
        """
        Display Name: Raw priority
        Default Value: 0
        Value Format: hex
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PriorityRaw']))

    @property
    def TosPrecedence(self):
        """
        Display Name: Precedence
        Default Value: 0
        Value Format: decimal
        Available enum values: 000 Routine, 0, 001 Priority, 1, 010 Immediate, 2, 011 Flash, 3, 100 Flash Override, 4, 101 CRITIC/ECP, 5, 110 Internetwork Control, 6, 111 Network Control, 7
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TosPrecedence']))

    @property
    def TosDelay(self):
        """
        Display Name: Delay
        Default Value: 0
        Value Format: decimal
        Available enum values: Normal, 0, Low, 1
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TosDelay']))

    @property
    def TosThroughput(self):
        """
        Display Name: Throughput
        Default Value: 0
        Value Format: decimal
        Available enum values: Normal, 0, High, 1
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TosThroughput']))

    @property
    def TosReliability(self):
        """
        Display Name: Reliability
        Default Value: 0
        Value Format: decimal
        Available enum values: Normal, 0, High, 1
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TosReliability']))

    @property
    def TosMonetary(self):
        """
        Display Name: Monetary
        Default Value: 0
        Value Format: decimal
        Available enum values: Normal, 0, Minimize, 1
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TosMonetary']))

    @property
    def TosUnused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TosUnused']))

    @property
    def DefaultPHBDefaultPHB(self):
        """
        Display Name: Default PHB
        Default Value: 0
        Value Format: decimal
        Available enum values: 0, 0
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DefaultPHBDefaultPHB']))

    @property
    def DefaultPHBUnused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DefaultPHBUnused']))

    @property
    def ClassSelectorPHBClassSelectorPHB(self):
        """
        Display Name: Class selector PHB
        Default Value: 8
        Value Format: decimal
        Available enum values: Precedence 1, 8, Precedence 2, 16, Precedence 3, 24, Precedence 4, 32, Precedence 5, 40, Precedence 6, 48, Precedence 7, 56
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ClassSelectorPHBClassSelectorPHB']))

    @property
    def ClassSelectorPHBUnused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ClassSelectorPHBUnused']))

    @property
    def AssuredForwardingPHBAssuredForwardingPHB(self):
        """
        Display Name: Assured forwarding PHB
        Default Value: 10
        Value Format: decimal
        Available enum values: Class 1, Low drop precedence, 10, Class 1, Medium drop precedence, 12, Class 1, High drop precedence, 14, Class 2, Low drop precedence, 18, Class 2, Medium drop precedence, 20, Class 2, High drop precedence, 22, Class 3, Low drop precedence, 26, Class 3, Medium drop precedence, 28, Class 3, High drop precedence, 30, Class 4, Low drop precedence, 34, Class 4, Medium drop precedence, 36, Class 4, High drop precedence, 38
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AssuredForwardingPHBAssuredForwardingPHB']))

    @property
    def AssuredForwardingPHBUnused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AssuredForwardingPHBUnused']))

    @property
    def ExpeditedForwardingPHBExpeditedForwardingPHB(self):
        """
        Display Name: Expedited forwarding PHB
        Default Value: 46
        Value Format: decimal
        Available enum values: 46, 46
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ExpeditedForwardingPHBExpeditedForwardingPHB']))

    @property
    def ExpeditedForwardingPHBUnused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: hex
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ExpeditedForwardingPHBUnused']))

    @property
    def TotalLength(self):
        """
        Display Name: Total Length (octets)
        Default Value: 20
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TotalLength']))

    @property
    def Identification(self):
        """
        Display Name: Identification
        Default Value: 0
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Identification']))

    @property
    def FlagsReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        Available enum values: 0, 0
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FlagsReserved']))

    @property
    def FlagsFragment(self):
        """
        Display Name: Fragment
        Default Value: 0
        Value Format: decimal
        Available enum values: May fragment, 0, Do not fragment, 1
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FlagsFragment']))

    @property
    def FlagsLastFragment(self):
        """
        Display Name: Last Fragment
        Default Value: 0
        Value Format: decimal
        Available enum values: Last fragment, 0, More fragments, 1
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FlagsLastFragment']))

    @property
    def FragmentOffset(self):
        """
        Display Name: Fragment offset
        Default Value: 0
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FragmentOffset']))

    @property
    def Ttl(self):
        """
        Display Name: TTL (Time to live)
        Default Value: 64
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Ttl']))

    @property
    def Protocol(self):
        """
        Display Name: Protocol
        Default Value: 61
        Value Format: decimal
        Available enum values: HOPOPT, 0, ICMP, 1, IGMP, 2, GGP, 3, IP, 4, ST, 5, TCP, 6, CBT, 7, EGP, 8, IGP, 9, BBN-RCC-MON, 10, NVP-II, 11, PUP, 12, ARGUS, 13, EMCON, 14, XNET, 15, CHAOS, 16, UDP, 17, MUX, 18, DCN-MEAS, 19, HMP, 20, PRM, 21, XNS-IDP, 22, TRUNK-1, 23, TRUNK-2, 24, LEAF-1, 25, LEAF-2, 26, RDP, 27, IRTP, 28, ISO-TP4, 29, NETBLT, 30, MFE-NSP, 31, MERIT-INP, 32, SEP, 33, 3PC, 34, IDPR, 35, XTP, 36, DDP, 37, IDPR-CMTP, 38, TP++, 39, IL, 40, IPv6, 41, SDRP, 42, IPv6-Route, 43, IPv6-Frag, 44, IDRP, 45, RSVP, 46, GRE, 47, MHRP, 48, BNA, 49, ESP, 50, AH, 51, I-NLSP, 52, SWIPE, 53, NARP, 54, MOBILE, 55, TLSP, 56, SKIP, 57, IPv6-ICMP, 58, IPv6-NoNxt, 59, IPv6-Opts, 60, Any host internal protocol, 61, CFTP, 62, Any local network, 63, SAT-EXPAK, 64, KRYPTOLAN, 65, RVD, 66, IPPC, 67, Any distributed file system, 68, SAT-MON, 69, VISA, 70, IPCV, 71, CPNX, 72, CPHB, 73, WSN, 74, PVP, 75, BR-SAT-MON, 76, SUN-ND, 77, WB-MON, 78, WB-EXPAK, 79, ISO-IP, 80, VMTP, 81, SECURE-VMTP, 82, VINES, 83, TTP, 84, NSFNET-IGP, 85, DGP, 86, TCF, 87, EIGRP, 88, OSPFIGP, 89, Sprite-RPC, 90, LARP, 91, MTP, 92, AX.25, 93, IPIP, 94, MICP, 95, SCC-SP, 96, ETHERIP, 97, ENCAP, 98, Any private encryption, 99, GMTP, 100, IFMP, 101, PNNI, 102, PIM, 103, ARIS, 104, SCPS, 105, QNX, 106, A/N, 107, IPComp, 108, SNP, 109, Compaq-Peer, 110, IPX-in-IP, 111, VRRP, 112, PGM, 113, Any 0-hop protocol, 114, L2TP, 115, DDX, 116, IATP, 117, STP, 118, SRP, 119, UTI, 120, SMP, 121, SM, 122, PTP, 123, ISIS over IPv4, 124, FIRE, 125, CRTP, 126, CRUDP, 127, SSCOPMCE, 128, IPLT, 129, SPS, 130, PIPE, 131, SCTP, 132, FC, 133, RSVP-E2E-IGNORE, 134, Mobility Header, 135, UDPLite, 136, MPLS-in-IP, 137, Unassigned, 138, Unassigned, 139, Unassigned, 140, Unassigned, 141, Unassigned, 142, Unassigned, 143, Unassigned, 144, Unassigned, 145, Unassigned, 146, Unassigned, 147, Unassigned, 148, Unassigned, 149, Unassigned, 150, Unassigned, 151, Unassigned, 152, Unassigned, 153, Unassigned, 154, Unassigned, 155, Unassigned, 156, Unassigned, 157, Unassigned, 158, Unassigned, 159, Unassigned, 160, Unassigned, 161, Unassigned, 162, Unassigned, 163, Unassigned, 164, Unassigned, 165, Unassigned, 166, Unassigned, 167, Unassigned, 168, Unassigned, 169, Unassigned, 170, Unassigned, 171, Unassigned, 172, Unassigned, 173, Unassigned, 174, Unassigned, 175, Unassigned, 176, Unassigned, 177, Unassigned, 178, Unassigned, 179, Unassigned, 180, Unassigned, 181, Unassigned, 182, Unassigned, 183, Unassigned, 184, Unassigned, 185, Unassigned, 186, Unassigned, 187, Unassigned, 188, Unassigned, 189, Unassigned, 190, Unassigned, 191, Unassigned, 192, Unassigned, 193, Unassigned, 194, Unassigned, 195, Unassigned, 196, Unassigned, 197, Unassigned, 198, Unassigned, 199, Unassigned, 200, Unassigned, 201, Unassigned, 202, Unassigned, 203, Unassigned, 204, Unassigned, 205, Unassigned, 206, Unassigned, 207, Unassigned, 208, Unassigned, 209, Unassigned, 210, Unassigned, 211, Unassigned, 212, Unassigned, 213, Unassigned, 214, Unassigned, 215, Unassigned, 216, Unassigned, 217, Unassigned, 218, Unassigned, 219, Unassigned, 220, Unassigned, 221, Unassigned, 222, Unassigned, 223, Unassigned, 224, Unassigned, 225, Unassigned, 226, Unassigned, 227, Unassigned, 228, Unassigned, 229, Unassigned, 230, Unassigned, 231, Unassigned, 232, Unassigned, 233, Unassigned, 234, Unassigned, 235, Unassigned, 236, Unassigned, 237, Unassigned, 238, Unassigned, 239, Unassigned, 240, Unassigned, 241, Unassigned, 242, Unassigned, 243, Unassigned, 244, Unassigned, 245, Unassigned, 246, Unassigned, 247, Unassigned, 248, Unassigned, 249, Unassigned, 250, Unassigned, 251, Unassigned, 252, Unassigned, 253, Unassigned, 254, Reserved, 255
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Protocol']))

    @property
    def Checksum(self):
        """
        Display Name: Header checksum
        Default Value: 0
        Value Format: hex
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Checksum']))

    @property
    def SrcIp(self):
        """
        Display Name: Source Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SrcIp']))

    @property
    def DstIp(self):
        """
        Display Name: Destination Address
        Default Value: 0.0.0.0
        Value Format: iPv4
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DstIp']))

    @property
    def OptionNop(self):
        """
        Display Name: No operation
        Default Value: 1
        Value Format: hex
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OptionNop']))

    @property
    def SecurityType(self):
        """
        Display Name: Security type
        Default Value: 130
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SecurityType']))

    @property
    def SecurityLength(self):
        """
        Display Name: Option length
        Default Value: 11
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SecurityLength']))

    @property
    def SecuritySecurity(self):
        """
        Display Name: Security
        Default Value: 0
        Value Format: decimal
        Available enum values: Unclassified, 0, Confidential, 61749, EFTO, 30874, MMMM, 48205, PROG, 24102, Restricted, 44819, Secret, 55176, Top Secret, 27589, 0x35e2 (Reserved for future use), 13794, 0x9af1 (Reserved for future use), 39665, 0x4d78 (Reserved for future use), 19832, 0x24bd (Reserved for future use), 9405, 0x135e (Reserved for future use), 4958, 0x89af (Reserved for future use), 35247, 0xc4d6 (Reserved for future use), 50390, 0xe26b (Reserved for future use), 57963
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SecuritySecurity']))

    @property
    def SecurityCompartments(self):
        """
        Display Name: Compartments
        Default Value: 0
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SecurityCompartments']))

    @property
    def SecurityHandling(self):
        """
        Display Name: Handling restrictions
        Default Value: 0
        Value Format: hex
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SecurityHandling']))

    @property
    def SecurityTcc(self):
        """
        Display Name: Transmission control code
        Default Value: 0
        Value Format: hex
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SecurityTcc']))

    @property
    def LsrrType(self):
        """
        Display Name: Option type
        Default Value: 131
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LsrrType']))

    @property
    def LsrrLength(self):
        """
        Display Name: Option length
        Default Value: 8
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LsrrLength']))

    @property
    def OptionPointer(self):
        """
        Display Name: Pointer
        Default Value: 4
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OptionPointer']))

    @property
    def OptionRouteData(self):
        """
        Display Name: Route data
        Default Value: 0
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OptionRouteData']))

    @property
    def SsrrType(self):
        """
        Display Name: Option type
        Default Value: 137
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SsrrType']))

    @property
    def SsrrLength(self):
        """
        Display Name: Option length
        Default Value: 8
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SsrrLength']))

    @property
    def RecordRouteType(self):
        """
        Display Name: Option type
        Default Value: 7
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RecordRouteType']))

    @property
    def RecordRouteLength(self):
        """
        Display Name: Option length
        Default Value: 8
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RecordRouteLength']))

    @property
    def StreamIdType(self):
        """
        Display Name: Option type
        Default Value: 136
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StreamIdType']))

    @property
    def StreamIdLength(self):
        """
        Display Name: Option length
        Default Value: 4
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StreamIdLength']))

    @property
    def StreamIdId(self):
        """
        Display Name: Stream identifier
        Default Value: 0
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StreamIdId']))

    @property
    def TimestampType(self):
        """
        Display Name: Option type
        Default Value: 68
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TimestampType']))

    @property
    def TimestampLength(self):
        """
        Display Name: Option length
        Default Value: 12
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TimestampLength']))

    @property
    def TimestampPointer(self):
        """
        Display Name: Pointer
        Default Value: 5
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TimestampPointer']))

    @property
    def TimestampOverflow(self):
        """
        Display Name: Overflow
        Default Value: 0
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TimestampOverflow']))

    @property
    def TimestampFlags(self):
        """
        Display Name: Flags
        Default Value: 0
        Value Format: decimal
        Available enum values: Timestamps only, in consecutive 32-bit words, 0, IP address, timestamp pairs, 1, IP addresses are prespecified, 3
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TimestampFlags']))

    @property
    def PairAddress(self):
        """
        Display Name: Address
        Default Value: 0
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PairAddress']))

    @property
    def PairTimestamp(self):
        """
        Display Name: Timestamp
        Default Value: 0
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PairTimestamp']))

    @property
    def OptionLast(self):
        """
        Display Name: End of options
        Default Value: 0
        Value Format: hex
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OptionLast']))

    @property
    def RouterAlertType(self):
        """
        Display Name: Option type
        Default Value: 0x94
        Value Format: hex
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RouterAlertType']))

    @property
    def RouterAlertLength(self):
        """
        Display Name: Option length
        Default Value: 0x04
        Value Format: decimal
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RouterAlertLength']))

    @property
    def RouterAlertValue(self):
        """
        Display Name: Router alert value
        Default Value: 0
        Value Format: decimal
        Available enum values: Router shall examine packet, 0
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RouterAlertValue']))

    @property
    def OptionsPad(self):
        """
        Display Name: Padding
        Default Value: 0
        Value Format: hex
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OptionsPad']))

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
