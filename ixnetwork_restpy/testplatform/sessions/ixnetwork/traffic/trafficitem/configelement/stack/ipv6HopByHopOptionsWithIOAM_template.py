from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ipv6HopByHopOptionsWithIOAM(Base):
    __slots__ = ()
    _SDM_NAME = "ipv6HopByHopOptionsWithIOAM"
    _SDM_ATT_MAP = {
        "HopByHopOptionsHeaderNextHeader": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.nextHeader-1",
        "HopByHopOptionsHeaderHeaderExtensionLength": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.headerExtensionLength-2",
        "TypeUnrecognizedType": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.userDefined.type.unrecognizedType-3",
        "TypeAllowPacketChange": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.userDefined.type.allowPacketChange-4",
        "TypeUserDefinedType": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.userDefined.type.userDefinedType-5",
        "UserDefinedLength": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.userDefined.length-6",
        "UserDefinedData": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.userDefined.data-7",
        "PadNType": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.padN.type-8",
        "PadNLength": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.padN.length-9",
        "PadNData": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.padN.data-10",
        "OptionPad1": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.pad1-11",
        "Incremental_tracing_optionOption_type_increemental": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.option_type_increemental-12",
        "Incremental_tracing_optionOptiondatalength": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.optiondatalength-13",
        "Incremental_tracing_optionReserved": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.reserved-14",
        "IoamtracetypeHoplim_nodeid_short": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioamtracetype.hoplim_nodeid_short-15",
        "IoamtracetypeIngress_egress_short": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioamtracetype.ingress_egress_short-16",
        "IoamtracetypeTimestamp_seconds": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioamtracetype.timestamp_seconds-17",
        "IoamtracetypeTimestamp_subseconds": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioamtracetype.timestamp_subseconds-18",
        "IoamtracetypeTransit_delay": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioamtracetype.transit_delay-19",
        "IoamtracetypeApp_data_short": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioamtracetype.app_data_short-20",
        "IoamtracetypeQueue_depth": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioamtracetype.queue_depth-21",
        "IoamtracetypeOpaque_state_snapshot": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioamtracetype.opaque_state_snapshot-22",
        "IoamtracetypeHoplim_nodeid_wide": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioamtracetype.hoplim_nodeid_wide-23",
        "IoamtracetypeIngress_egress_wide": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioamtracetype.ingress_egress_wide-24",
        "IoamtracetypeApp_data_wide": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioamtracetype.app_data_wide-25",
        "IoamtracetypeChecksum_complement": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioamtracetype.checksum_complement-26",
        "IoamtracetypeUndefined01": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioamtracetype.undefined01-27",
        "IoamtracetypeUndefined02": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioamtracetype.undefined02-28",
        "IoamtracetypeUndefined03": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioamtracetype.undefined03-29",
        "IoamtracetypeUndefined04": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioamtracetype.undefined04-30",
        "Incree_option_dataNode_length": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.node_length-31",
        "FlagsOverflow": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.flags.overflow-32",
        "FlagsLoopback": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.flags.loopback-33",
        "FlagsReserved01": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.flags.reserved01-34",
        "FlagsReserved02": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.flags.reserved02-35",
        "Incree_option_dataMaximumlength": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.maximumlength-36",
        "Hopnode_short32Hoplim_short": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioam_node_data.hopnode_short32.hoplim_short-37",
        "Hopnode_short32Nodeid_short": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioam_node_data.hopnode_short32.nodeid_short-38",
        "Ingress_egress_short32Ingress_short": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioam_node_data.ingress_egress_short32.ingress_short-39",
        "Ingress_egress_short32Egress_short": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioam_node_data.ingress_egress_short32.egress_short-40",
        "Ioam_node_dataTimestamp_seconds_32": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioam_node_data.timestamp_seconds_32-41",
        "Ioam_node_dataTimestamp_subseconds32": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioam_node_data.timestamp_subseconds32-42",
        "Transit_delay32Transit_overflow": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioam_node_data.transit_delay32.transit_overflow-43",
        "Transit_delay32Transit_delay32": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioam_node_data.transit_delay32.transit_delay32-44",
        "Ioam_node_dataApp_data_short32": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioam_node_data.app_data_short32-45",
        "Ioam_node_dataQueue_depth32": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioam_node_data.queue_depth32-46",
        "Opaque_state_snapshot32Opaque_length": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioam_node_data.opaque_state_snapshot32.opaque_length-47",
        "Opaque_state_snapshot32Schema_id": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioam_node_data.opaque_state_snapshot32.schema_id-48",
        "Opaque_state_snapshot32Opaque_data": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioam_node_data.opaque_state_snapshot32.opaque_data-49",
        "Hopnode_wide64Hoplim_wide": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioam_node_data.hopnode_wide64.hoplim_wide-50",
        "Hopnode_wide64Nodeid_wide": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioam_node_data.hopnode_wide64.nodeid_wide-51",
        "Ingress_egress_wide64Ingress_wide": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioam_node_data.ingress_egress_wide64.ingress_wide-52",
        "Ingress_egress_wide64Egress_wide": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioam_node_data.ingress_egress_wide64.egress_wide-53",
        "Ioam_node_dataApp_data_short64": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioam_node_data.app_data_short64-54",
        "Checksum_complementChecksum_complement16": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioam_node_data.checksum_complement.checksum_complement16-55",
        "Checksum_complementReserved16": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.incremental_tracing_option.incree_option_data.ioam_node_data.checksum_complement.reserved16-56",
        "Preallocated_tracing_optionOption_type_preallocated": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.option_type_preallocated-57",
        "Preallocated_tracing_optionOptiondatalength": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.optiondatalength-58",
        "Preallocated_tracing_optionReserved": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.reserved-59",
        "DataIoamtracetypeHoplim_nodeid_short": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioamtracetype.hoplim_nodeid_short-60",
        "DataIoamtracetypeIngress_egress_short": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioamtracetype.ingress_egress_short-61",
        "DataIoamtracetypeTimestamp_seconds": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioamtracetype.timestamp_seconds-62",
        "DataIoamtracetypeTimestamp_subseconds": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioamtracetype.timestamp_subseconds-63",
        "DataIoamtracetypeTransit_delay": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioamtracetype.transit_delay-64",
        "DataIoamtracetypeApp_data_short": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioamtracetype.app_data_short-65",
        "DataIoamtracetypeQueue_depth": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioamtracetype.queue_depth-66",
        "DataIoamtracetypeOpaque_state_snapshot": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioamtracetype.opaque_state_snapshot-67",
        "DataIoamtracetypeHoplim_nodeid_wide": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioamtracetype.hoplim_nodeid_wide-68",
        "DataIoamtracetypeIngress_egress_wide": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioamtracetype.ingress_egress_wide-69",
        "DataIoamtracetypeApp_data_wide": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioamtracetype.app_data_wide-70",
        "DataIoamtracetypeChecksum_complement": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioamtracetype.checksum_complement-71",
        "DataIoamtracetypeUndefined01": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioamtracetype.undefined01-72",
        "DataIoamtracetypeUndefined02": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioamtracetype.undefined02-73",
        "DataIoamtracetypeUndefined03": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioamtracetype.undefined03-74",
        "DataIoamtracetypeUndefined04": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioamtracetype.undefined04-75",
        "DataNode_length": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.node_length-76",
        "DataFlagsOverflow": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.flags.overflow-77",
        "DataFlagsLoopback": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.flags.loopback-78",
        "DataFlagsReserved01": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.flags.reserved01-79",
        "DataFlagsReserved02": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.flags.reserved02-80",
        "DataRemaininglength": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.remaininglength-81",
        "DataPreallocatedemptyblock": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.preallocatedemptyblock-82",
        "Ioam_node_dataHopnode_short32Hoplim_short": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioam_node_data.hopnode_short32.hoplim_short-83",
        "Ioam_node_dataHopnode_short32Nodeid_short": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioam_node_data.hopnode_short32.nodeid_short-84",
        "Ioam_node_dataIngress_egress_short32Ingress_short": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioam_node_data.ingress_egress_short32.ingress_short-85",
        "Ioam_node_dataIngress_egress_short32Egress_short": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioam_node_data.ingress_egress_short32.egress_short-86",
        "DataIoam_node_dataTimestamp_seconds_32": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioam_node_data.timestamp_seconds_32-87",
        "DataIoam_node_dataTimestamp_subseconds32": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioam_node_data.timestamp_subseconds32-88",
        "Ioam_node_dataTransit_delay32Transit_overflow": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioam_node_data.transit_delay32.transit_overflow-89",
        "Ioam_node_dataTransit_delay32Transit_delay32": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioam_node_data.transit_delay32.transit_delay32-90",
        "DataIoam_node_dataApp_data_short32": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioam_node_data.app_data_short32-91",
        "DataIoam_node_dataQueue_depth32": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioam_node_data.queue_depth32-92",
        "Ioam_node_dataOpaque_state_snapshot32Opaque_length": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioam_node_data.opaque_state_snapshot32.opaque_length-93",
        "Ioam_node_dataOpaque_state_snapshot32Schema_id": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioam_node_data.opaque_state_snapshot32.schema_id-94",
        "Ioam_node_dataOpaque_state_snapshot32Opaque_data": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioam_node_data.opaque_state_snapshot32.opaque_data-95",
        "Ioam_node_dataHopnode_wide64Hoplim_wide": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioam_node_data.hopnode_wide64.hoplim_wide-96",
        "Ioam_node_dataHopnode_wide64Nodeid_wide": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioam_node_data.hopnode_wide64.nodeid_wide-97",
        "Ioam_node_dataIngress_egress_wide64Ingress_wide": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioam_node_data.ingress_egress_wide64.ingress_wide-98",
        "Ioam_node_dataIngress_egress_wide64Egress_wide": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioam_node_data.ingress_egress_wide64.egress_wide-99",
        "DataIoam_node_dataApp_data_short64": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioam_node_data.app_data_short64-100",
        "Ioam_node_dataChecksum_complementChecksum_complement16": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioam_node_data.checksum_complement.checksum_complement16-101",
        "Ioam_node_dataChecksum_complementReserved16": "ipv6HopByHopOptionsWithIOAM.header.hopByHopOptionsHeader.options.option.preallocated_tracing_option.data.ioam_node_data.checksum_complement.reserved16-102",
        "HeaderPad": "ipv6HopByHopOptionsWithIOAM.header.pad-103",
    }

    def __init__(self, parent, list_op=False):
        super(Ipv6HopByHopOptionsWithIOAM, self).__init__(parent, list_op)

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
        Available enum values: Option Data can change en-route, 0, Option Data cannot change en-route, 1
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
    def Incremental_tracing_optionOption_type_increemental(self):
        """
        Display Name: Option Type (Incremental)
        Default Value: 0x20
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Incremental_tracing_optionOption_type_increemental"]
            ),
        )

    @property
    def Incremental_tracing_optionOptiondatalength(self):
        """
        Display Name: Option Data Length (Octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Incremental_tracing_optionOptiondatalength"]
            ),
        )

    @property
    def Incremental_tracing_optionReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Incremental_tracing_optionReserved"]
            ),
        )

    @property
    def IoamtracetypeHoplim_nodeid_short(self):
        """
        Display Name: Hop Limit-Node Id (Short)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["IoamtracetypeHoplim_nodeid_short"]),
        )

    @property
    def IoamtracetypeIngress_egress_short(self):
        """
        Display Name: Ingress-Egress If Id (Short)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["IoamtracetypeIngress_egress_short"]),
        )

    @property
    def IoamtracetypeTimestamp_seconds(self):
        """
        Display Name: Timestamp Seconds
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["IoamtracetypeTimestamp_seconds"]),
        )

    @property
    def IoamtracetypeTimestamp_subseconds(self):
        """
        Display Name: Timestamp Subseconds
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["IoamtracetypeTimestamp_subseconds"]),
        )

    @property
    def IoamtracetypeTransit_delay(self):
        """
        Display Name: Transit Delay
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IoamtracetypeTransit_delay"])
        )

    @property
    def IoamtracetypeApp_data_short(self):
        """
        Display Name: App Data (Short)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IoamtracetypeApp_data_short"])
        )

    @property
    def IoamtracetypeQueue_depth(self):
        """
        Display Name: Queue Depth
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IoamtracetypeQueue_depth"])
        )

    @property
    def IoamtracetypeOpaque_state_snapshot(self):
        """
        Display Name: Variable Length Opaque State Snapshot
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["IoamtracetypeOpaque_state_snapshot"]
            ),
        )

    @property
    def IoamtracetypeHoplim_nodeid_wide(self):
        """
        Display Name: Hop Limit-Node Id (Wide)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["IoamtracetypeHoplim_nodeid_wide"]),
        )

    @property
    def IoamtracetypeIngress_egress_wide(self):
        """
        Display Name: Ingress-Egress If Id (Wide)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["IoamtracetypeIngress_egress_wide"]),
        )

    @property
    def IoamtracetypeApp_data_wide(self):
        """
        Display Name: App Data (Wide)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IoamtracetypeApp_data_wide"])
        )

    @property
    def IoamtracetypeChecksum_complement(self):
        """
        Display Name: Checksum Complement
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["IoamtracetypeChecksum_complement"]),
        )

    @property
    def IoamtracetypeUndefined01(self):
        """
        Display Name: Undefined
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IoamtracetypeUndefined01"])
        )

    @property
    def IoamtracetypeUndefined02(self):
        """
        Display Name: Undefined
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IoamtracetypeUndefined02"])
        )

    @property
    def IoamtracetypeUndefined03(self):
        """
        Display Name: Undefined
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IoamtracetypeUndefined03"])
        )

    @property
    def IoamtracetypeUndefined04(self):
        """
        Display Name: Undefined
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["IoamtracetypeUndefined04"])
        )

    @property
    def Incree_option_dataNode_length(self):
        """
        Display Name: Node Data Length (x4 Octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Incree_option_dataNode_length"]),
        )

    @property
    def FlagsOverflow(self):
        """
        Display Name: Overflow
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FlagsOverflow"]))

    @property
    def FlagsLoopback(self):
        """
        Display Name: Loopback
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["FlagsLoopback"]))

    @property
    def FlagsReserved01(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsReserved01"])
        )

    @property
    def FlagsReserved02(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["FlagsReserved02"])
        )

    @property
    def Incree_option_dataMaximumlength(self):
        """
        Display Name: Maximum Length (x4 Octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Incree_option_dataMaximumlength"]),
        )

    @property
    def Hopnode_short32Hoplim_short(self):
        """
        Display Name: Hop Limit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Hopnode_short32Hoplim_short"])
        )

    @property
    def Hopnode_short32Nodeid_short(self):
        """
        Display Name: Node Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Hopnode_short32Nodeid_short"])
        )

    @property
    def Ingress_egress_short32Ingress_short(self):
        """
        Display Name: Ingress If Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ingress_egress_short32Ingress_short"]
            ),
        )

    @property
    def Ingress_egress_short32Egress_short(self):
        """
        Display Name: Egress If Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ingress_egress_short32Egress_short"]
            ),
        )

    @property
    def Ioam_node_dataTimestamp_seconds_32(self):
        """
        Display Name: Timestamp Seconds
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ioam_node_dataTimestamp_seconds_32"]
            ),
        )

    @property
    def Ioam_node_dataTimestamp_subseconds32(self):
        """
        Display Name: Timestamp Subseconds
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ioam_node_dataTimestamp_subseconds32"]
            ),
        )

    @property
    def Transit_delay32Transit_overflow(self):
        """
        Display Name: Overflow
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Transit_delay32Transit_overflow"]),
        )

    @property
    def Transit_delay32Transit_delay32(self):
        """
        Display Name: Transit Delay
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Transit_delay32Transit_delay32"]),
        )

    @property
    def Ioam_node_dataApp_data_short32(self):
        """
        Display Name: App Data(Short)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ioam_node_dataApp_data_short32"]),
        )

    @property
    def Ioam_node_dataQueue_depth32(self):
        """
        Display Name: Queue Depth
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Ioam_node_dataQueue_depth32"])
        )

    @property
    def Opaque_state_snapshot32Opaque_length(self):
        """
        Display Name: Length (x4 Octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Opaque_state_snapshot32Opaque_length"]
            ),
        )

    @property
    def Opaque_state_snapshot32Schema_id(self):
        """
        Display Name: Schema Id
        Default Value: 0xFFFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Opaque_state_snapshot32Schema_id"]),
        )

    @property
    def Opaque_state_snapshot32Opaque_data(self):
        """
        Display Name: Opaque Data
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Opaque_state_snapshot32Opaque_data"]
            ),
        )

    @property
    def Hopnode_wide64Hoplim_wide(self):
        """
        Display Name: Hop Limit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Hopnode_wide64Hoplim_wide"])
        )

    @property
    def Hopnode_wide64Nodeid_wide(self):
        """
        Display Name: Node Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Hopnode_wide64Nodeid_wide"])
        )

    @property
    def Ingress_egress_wide64Ingress_wide(self):
        """
        Display Name: Ingress If Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ingress_egress_wide64Ingress_wide"]),
        )

    @property
    def Ingress_egress_wide64Egress_wide(self):
        """
        Display Name: Egress If Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ingress_egress_wide64Egress_wide"]),
        )

    @property
    def Ioam_node_dataApp_data_short64(self):
        """
        Display Name: App Data(Wide)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Ioam_node_dataApp_data_short64"]),
        )

    @property
    def Checksum_complementChecksum_complement16(self):
        """
        Display Name: Checksum Complement
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Checksum_complementChecksum_complement16"]
            ),
        )

    @property
    def Checksum_complementReserved16(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["Checksum_complementReserved16"]),
        )

    @property
    def Preallocated_tracing_optionOption_type_preallocated(self):
        """
        Display Name: Option Type (Pre-allocated)
        Default Value: 0x21
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Preallocated_tracing_optionOption_type_preallocated"]
            ),
        )

    @property
    def Preallocated_tracing_optionOptiondatalength(self):
        """
        Display Name: Option Data Length (Octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Preallocated_tracing_optionOptiondatalength"]
            ),
        )

    @property
    def Preallocated_tracing_optionReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Preallocated_tracing_optionReserved"]
            ),
        )

    @property
    def DataIoamtracetypeHoplim_nodeid_short(self):
        """
        Display Name: Hop Limit-Node Id (Short)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DataIoamtracetypeHoplim_nodeid_short"]
            ),
        )

    @property
    def DataIoamtracetypeIngress_egress_short(self):
        """
        Display Name: Ingress-Egress If Id (Short)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DataIoamtracetypeIngress_egress_short"]
            ),
        )

    @property
    def DataIoamtracetypeTimestamp_seconds(self):
        """
        Display Name: Timestamp Seconds
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DataIoamtracetypeTimestamp_seconds"]
            ),
        )

    @property
    def DataIoamtracetypeTimestamp_subseconds(self):
        """
        Display Name: Timestamp Subseconds
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DataIoamtracetypeTimestamp_subseconds"]
            ),
        )

    @property
    def DataIoamtracetypeTransit_delay(self):
        """
        Display Name: Transit Delay
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["DataIoamtracetypeTransit_delay"]),
        )

    @property
    def DataIoamtracetypeApp_data_short(self):
        """
        Display Name: App Data (Short)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["DataIoamtracetypeApp_data_short"]),
        )

    @property
    def DataIoamtracetypeQueue_depth(self):
        """
        Display Name: Queue Depth
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataIoamtracetypeQueue_depth"])
        )

    @property
    def DataIoamtracetypeOpaque_state_snapshot(self):
        """
        Display Name: Variable Length Opaque State Snapshot
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DataIoamtracetypeOpaque_state_snapshot"]
            ),
        )

    @property
    def DataIoamtracetypeHoplim_nodeid_wide(self):
        """
        Display Name: Hop Limit-Node Id (Wide)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DataIoamtracetypeHoplim_nodeid_wide"]
            ),
        )

    @property
    def DataIoamtracetypeIngress_egress_wide(self):
        """
        Display Name: Ingress-Egress If Id (Wide)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DataIoamtracetypeIngress_egress_wide"]
            ),
        )

    @property
    def DataIoamtracetypeApp_data_wide(self):
        """
        Display Name: App Data (Wide)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["DataIoamtracetypeApp_data_wide"]),
        )

    @property
    def DataIoamtracetypeChecksum_complement(self):
        """
        Display Name: Checksum Complement
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DataIoamtracetypeChecksum_complement"]
            ),
        )

    @property
    def DataIoamtracetypeUndefined01(self):
        """
        Display Name: Undefined
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataIoamtracetypeUndefined01"])
        )

    @property
    def DataIoamtracetypeUndefined02(self):
        """
        Display Name: Undefined
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataIoamtracetypeUndefined02"])
        )

    @property
    def DataIoamtracetypeUndefined03(self):
        """
        Display Name: Undefined
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataIoamtracetypeUndefined03"])
        )

    @property
    def DataIoamtracetypeUndefined04(self):
        """
        Display Name: Undefined
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataIoamtracetypeUndefined04"])
        )

    @property
    def DataNode_length(self):
        """
        Display Name: Node Data Length (x4 Octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataNode_length"])
        )

    @property
    def DataFlagsOverflow(self):
        """
        Display Name: Overflow
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataFlagsOverflow"])
        )

    @property
    def DataFlagsLoopback(self):
        """
        Display Name: Loopback
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataFlagsLoopback"])
        )

    @property
    def DataFlagsReserved01(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataFlagsReserved01"])
        )

    @property
    def DataFlagsReserved02(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataFlagsReserved02"])
        )

    @property
    def DataRemaininglength(self):
        """
        Display Name: Remaining Length (x4 Octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataRemaininglength"])
        )

    @property
    def DataPreallocatedemptyblock(self):
        """
        Display Name: Pre-Allocated Empty Block (x4 octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["DataPreallocatedemptyblock"])
        )

    @property
    def Ioam_node_dataHopnode_short32Hoplim_short(self):
        """
        Display Name: Hop Limit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ioam_node_dataHopnode_short32Hoplim_short"]
            ),
        )

    @property
    def Ioam_node_dataHopnode_short32Nodeid_short(self):
        """
        Display Name: Node Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ioam_node_dataHopnode_short32Nodeid_short"]
            ),
        )

    @property
    def Ioam_node_dataIngress_egress_short32Ingress_short(self):
        """
        Display Name: Ingress If Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ioam_node_dataIngress_egress_short32Ingress_short"]
            ),
        )

    @property
    def Ioam_node_dataIngress_egress_short32Egress_short(self):
        """
        Display Name: Egress If Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ioam_node_dataIngress_egress_short32Egress_short"]
            ),
        )

    @property
    def DataIoam_node_dataTimestamp_seconds_32(self):
        """
        Display Name: Timestamp Seconds
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DataIoam_node_dataTimestamp_seconds_32"]
            ),
        )

    @property
    def DataIoam_node_dataTimestamp_subseconds32(self):
        """
        Display Name: Timestamp Subseconds
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DataIoam_node_dataTimestamp_subseconds32"]
            ),
        )

    @property
    def Ioam_node_dataTransit_delay32Transit_overflow(self):
        """
        Display Name: Overflow
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ioam_node_dataTransit_delay32Transit_overflow"]
            ),
        )

    @property
    def Ioam_node_dataTransit_delay32Transit_delay32(self):
        """
        Display Name: Transit Delay
        Default Value: 0xFFFFFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ioam_node_dataTransit_delay32Transit_delay32"]
            ),
        )

    @property
    def DataIoam_node_dataApp_data_short32(self):
        """
        Display Name: App Data(Short)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DataIoam_node_dataApp_data_short32"]
            ),
        )

    @property
    def DataIoam_node_dataQueue_depth32(self):
        """
        Display Name: Queue Depth
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["DataIoam_node_dataQueue_depth32"]),
        )

    @property
    def Ioam_node_dataOpaque_state_snapshot32Opaque_length(self):
        """
        Display Name: Length (x4 Octets)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ioam_node_dataOpaque_state_snapshot32Opaque_length"]
            ),
        )

    @property
    def Ioam_node_dataOpaque_state_snapshot32Schema_id(self):
        """
        Display Name: Schema Id
        Default Value: 0xFFFFFF
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ioam_node_dataOpaque_state_snapshot32Schema_id"]
            ),
        )

    @property
    def Ioam_node_dataOpaque_state_snapshot32Opaque_data(self):
        """
        Display Name: Opaque Data
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ioam_node_dataOpaque_state_snapshot32Opaque_data"]
            ),
        )

    @property
    def Ioam_node_dataHopnode_wide64Hoplim_wide(self):
        """
        Display Name: Hop Limit
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ioam_node_dataHopnode_wide64Hoplim_wide"]
            ),
        )

    @property
    def Ioam_node_dataHopnode_wide64Nodeid_wide(self):
        """
        Display Name: Node Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ioam_node_dataHopnode_wide64Nodeid_wide"]
            ),
        )

    @property
    def Ioam_node_dataIngress_egress_wide64Ingress_wide(self):
        """
        Display Name: Ingress If Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ioam_node_dataIngress_egress_wide64Ingress_wide"]
            ),
        )

    @property
    def Ioam_node_dataIngress_egress_wide64Egress_wide(self):
        """
        Display Name: Egress If Id
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ioam_node_dataIngress_egress_wide64Egress_wide"]
            ),
        )

    @property
    def DataIoam_node_dataApp_data_short64(self):
        """
        Display Name: App Data(Wide)
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DataIoam_node_dataApp_data_short64"]
            ),
        )

    @property
    def Ioam_node_dataChecksum_complementChecksum_complement16(self):
        """
        Display Name: Checksum Complement
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "Ioam_node_dataChecksum_complementChecksum_complement16"
                ]
            ),
        )

    @property
    def Ioam_node_dataChecksum_complementReserved16(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["Ioam_node_dataChecksum_complementReserved16"]
            ),
        )

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
