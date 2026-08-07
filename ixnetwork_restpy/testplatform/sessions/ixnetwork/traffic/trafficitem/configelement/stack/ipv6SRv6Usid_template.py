from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Ipv6SRv6Usid(Base):
    __slots__ = ()
    _SDM_NAME = "ipv6SRv6Usid"
    _SDM_ATT_MAP = {
        "VersionTCFLVersion": "ipv6SRv6Usid.header.versionTCFL.version-1",
        "VersionTCFLTrafficClass": "ipv6SRv6Usid.header.versionTCFL.trafficClass-2",
        "VersionTCFLFlowLabel": "ipv6SRv6Usid.header.versionTCFL.flowLabel-3",
        "HeaderPayloadLength": "ipv6SRv6Usid.header.payloadLength-4",
        "HeaderNextHeader": "ipv6SRv6Usid.header.nextHeader-5",
        "HeaderHopLimit": "ipv6SRv6Usid.header.hopLimit-6",
        "HeaderSrcIP": "ipv6SRv6Usid.header.srcIP-7",
        "Da_fmtDa_full": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_full-8",
        "Da_l16_0_16Lb_l16_0_16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l16_0_16.lb_l16_0_16-9",
        "Da_l16_0_16U0_l16_0_16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l16_0_16.u0_l16_0_16-10",
        "Da_l16_0_16U1_l16_0_16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l16_0_16.u1_l16_0_16-11",
        "Da_l16_0_16U2_l16_0_16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l16_0_16.u2_l16_0_16-12",
        "Da_l16_0_16U3_l16_0_16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l16_0_16.u3_l16_0_16-13",
        "Da_l16_0_16U4_l16_0_16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l16_0_16.u4_l16_0_16-14",
        "Da_l16_0_16U5_l16_0_16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l16_0_16.u5_l16_0_16-15",
        "Da_l16_0_16U6_l16_0_16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l16_0_16.u6_l16_0_16-16",
        "Da_l32_16_16LocatorBlock": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l32_16_16.locatorBlock-17",
        "Da_l32_16_16ActiveUSID": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l32_16_16.activeUSID-18",
        "Da_l32_16_16NextUSID0": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l32_16_16.nextUSID0-19",
        "Da_l32_16_16NextUSID1": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l32_16_16.nextUSID1-20",
        "Da_l32_16_16NextUSID2": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l32_16_16.nextUSID2-21",
        "Da_l32_16_16NextUSID3": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l32_16_16.nextUSID3-22",
        "Da_l32_16_16EomUSID": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l32_16_16.eomUSID-23",
        "Da_l48_16_16Lb_l48_16_16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l48_16_16.lb_l48_16_16-24",
        "Da_l48_16_16U0_l48_16_16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l48_16_16.u0_l48_16_16-25",
        "Da_l48_16_16U1_l48_16_16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l48_16_16.u1_l48_16_16-26",
        "Da_l48_16_16U2_l48_16_16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l48_16_16.u2_l48_16_16-27",
        "Da_l48_16_16U3_l48_16_16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l48_16_16.u3_l48_16_16-28",
        "Da_l48_16_16U4_l48_16_16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l48_16_16.u4_l48_16_16-29",
        "Da_l64_0_16Lb_l64_0_16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l64_0_16.lb_l64_0_16-30",
        "Da_l64_0_16U0_l64_0_16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l64_0_16.u0_l64_0_16-31",
        "Da_l64_0_16U1_l64_0_16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l64_0_16.u1_l64_0_16-32",
        "Da_l64_0_16U2_l64_0_16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l64_0_16.u2_l64_0_16-33",
        "Da_l64_0_16U3_l64_0_16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l64_0_16.u3_l64_0_16-34",
        "Da_l80_0_16Lb_l80_0_16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l80_0_16.lb_l80_0_16-35",
        "Da_l80_0_16U0_l80_0_16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l80_0_16.u0_l80_0_16-36",
        "Da_l80_0_16U1_l80_0_16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l80_0_16.u1_l80_0_16-37",
        "Da_l80_0_16U2_l80_0_16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l80_0_16.u2_l80_0_16-38",
        "Da_l96_0_16Lb_l96_0_16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l96_0_16.lb_l96_0_16-39",
        "Da_l96_0_16U0_l96_0_16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l96_0_16.u0_l96_0_16-40",
        "Da_l96_0_16U1_l96_0_16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l96_0_16.u1_l96_0_16-41",
        "Da_l16_0_8Lb_l16_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l16_0_8.lb_l16_0_8-42",
        "Da_l16_0_8U0_l16_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l16_0_8.u0_l16_0_8-43",
        "Da_l16_0_8U1_l16_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l16_0_8.u1_l16_0_8-44",
        "Da_l16_0_8U2_l16_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l16_0_8.u2_l16_0_8-45",
        "Da_l16_0_8U3_l16_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l16_0_8.u3_l16_0_8-46",
        "Da_l16_0_8U4_l16_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l16_0_8.u4_l16_0_8-47",
        "Da_l16_0_8U5_l16_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l16_0_8.u5_l16_0_8-48",
        "Da_l16_0_8U6_l16_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l16_0_8.u6_l16_0_8-49",
        "Da_l16_0_8U7_l16_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l16_0_8.u7_l16_0_8-50",
        "Da_l16_0_8U8_l16_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l16_0_8.u8_l16_0_8-51",
        "Da_l16_0_8U9_l16_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l16_0_8.u9_l16_0_8-52",
        "Da_l16_0_8U10_l16_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l16_0_8.u10_l16_0_8-53",
        "Da_l16_0_8U11_l16_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l16_0_8.u11_l16_0_8-54",
        "Da_l16_0_8U12_l16_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l16_0_8.u12_l16_0_8-55",
        "Da_l16_0_8U13_l16_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l16_0_8.u13_l16_0_8-56",
        "Da_l32_16_8Lb_l32_16_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l32_16_8.lb_l32_16_8-57",
        "Da_l32_16_8U0_l32_16_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l32_16_8.u0_l32_16_8-58",
        "Da_l32_16_8U1_l32_16_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l32_16_8.u1_l32_16_8-59",
        "Da_l32_16_8U2_l32_16_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l32_16_8.u2_l32_16_8-60",
        "Da_l32_16_8U3_l32_16_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l32_16_8.u3_l32_16_8-61",
        "Da_l32_16_8U4_l32_16_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l32_16_8.u4_l32_16_8-62",
        "Da_l32_16_8U5_l32_16_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l32_16_8.u5_l32_16_8-63",
        "Da_l32_16_8U6_l32_16_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l32_16_8.u6_l32_16_8-64",
        "Da_l32_16_8U7_l32_16_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l32_16_8.u7_l32_16_8-65",
        "Da_l32_16_8U8_l32_16_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l32_16_8.u8_l32_16_8-66",
        "Da_l32_16_8U9_l32_16_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l32_16_8.u9_l32_16_8-67",
        "Da_l32_16_8U10_l32_16_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l32_16_8.u10_l32_16_8-68",
        "Da_l32_16_8U11_l32_16_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l32_16_8.u11_l32_16_8-69",
        "Da_l48_0_8Lb_l48_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l48_0_8.lb_l48_0_8-70",
        "Da_l48_0_8U0_l48_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l48_0_8.u0_l48_0_8-71",
        "Da_l48_0_8U1_l48_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l48_0_8.u1_l48_0_8-72",
        "Da_l48_0_8U2_l48_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l48_0_8.u2_l48_0_8-73",
        "Da_l48_0_8U3_l48_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l48_0_8.u3_l48_0_8-74",
        "Da_l48_0_8U4_l48_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l48_0_8.u4_l48_0_8-75",
        "Da_l48_0_8U5_l48_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l48_0_8.u5_l48_0_8-76",
        "Da_l48_0_8U6_l48_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l48_0_8.u6_l48_0_8-77",
        "Da_l48_0_8U7_l48_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l48_0_8.u7_l48_0_8-78",
        "Da_l48_0_8U8_l48_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l48_0_8.u8_l48_0_8-79",
        "Da_l48_0_8U9_l48_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l48_0_8.u9_l48_0_8-80",
        "Da_l64_0_8Lb_l64_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l64_0_8.lb_l64_0_8-81",
        "Da_l64_0_8U0_l64_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l64_0_8.u0_l64_0_8-82",
        "Da_l64_0_8U1_l64_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l64_0_8.u1_l64_0_8-83",
        "Da_l64_0_8U2_l64_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l64_0_8.u2_l64_0_8-84",
        "Da_l64_0_8U3_l64_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l64_0_8.u3_l64_0_8-85",
        "Da_l64_0_8U4_l64_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l64_0_8.u4_l64_0_8-86",
        "Da_l64_0_8U5_l64_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l64_0_8.u5_l64_0_8-87",
        "Da_l64_0_8U6_l64_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l64_0_8.u6_l64_0_8-88",
        "Da_l64_0_8U7_l64_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l64_0_8.u7_l64_0_8-89",
        "Da_l80_0_8Lb_l80_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l80_0_8.lb_l80_0_8-90",
        "Da_l80_0_8U0_l80_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l80_0_8.u0_l80_0_8-91",
        "Da_l80_0_8U1_l80_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l80_0_8.u1_l80_0_8-92",
        "Da_l80_0_8U2_l80_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l80_0_8.u2_l80_0_8-93",
        "Da_l80_0_8U3_l80_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l80_0_8.u3_l80_0_8-94",
        "Da_l80_0_8U4_l80_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l80_0_8.u4_l80_0_8-95",
        "Da_l80_0_8U5_l80_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l80_0_8.u5_l80_0_8-96",
        "Da_l96_0_8Lb_l96_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l96_0_8.lb_l96_0_8-97",
        "Da_l96_0_8U0_l96_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l96_0_8.u0_l96_0_8-98",
        "Da_l96_0_8U1_l96_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l96_0_8.u1_l96_0_8-99",
        "Da_l96_0_8U2_l96_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l96_0_8.u2_l96_0_8-100",
        "Da_l96_0_8U3_l96_0_8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l96_0_8.u3_l96_0_8-101",
        "Da_l32_0_32Lb_l32_0_32": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l32_0_32.lb_l32_0_32-102",
        "Da_l32_0_32U0_l32_0_32": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l32_0_32.u0_l32_0_32-103",
        "Da_l32_0_32U1_l32_0_32": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l32_0_32.u1_l32_0_32-104",
        "Da_l32_0_32U2_l32_0_32": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l32_0_32.u2_l32_0_32-105",
        "Da_l64_0_32Lb_l64_0_32": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l64_0_32.lb_l64_0_32-106",
        "Da_l64_0_32U0_l64_0_32": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l64_0_32.u0_l64_0_32-107",
        "Da_l64_0_32U1_l64_0_32": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l64_0_32.u1_l64_0_32-108",
        "Da_l96_0_32Lb_l96_0_32": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l96_0_32.lb_l96_0_32-109",
        "Da_l96_0_32U0_l96_0_32": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_l96_0_32.u0_l96_0_32-110",
        "Da_s16Da_u0_s16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_s16.da_u0_s16-111",
        "Da_s16Da_u1_s16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_s16.da_u1_s16-112",
        "Da_s16Da_u2_s16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_s16.da_u2_s16-113",
        "Da_s16Da_u3_s16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_s16.da_u3_s16-114",
        "Da_s16Da_u4_s16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_s16.da_u4_s16-115",
        "Da_s16Da_u5_s16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_s16.da_u5_s16-116",
        "Da_s16Da_u6_s16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_s16.da_u6_s16-117",
        "Da_s16Da_u7_s16": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_s16.da_u7_s16-118",
        "Da_s8Da_u0_s8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_s8.da_u0_s8-119",
        "Da_s8Da_u1_s8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_s8.da_u1_s8-120",
        "Da_s8Da_u2_s8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_s8.da_u2_s8-121",
        "Da_s8Da_u3_s8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_s8.da_u3_s8-122",
        "Da_s8Da_u4_s8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_s8.da_u4_s8-123",
        "Da_s8Da_u5_s8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_s8.da_u5_s8-124",
        "Da_s8Da_u6_s8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_s8.da_u6_s8-125",
        "Da_s8Da_u7_s8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_s8.da_u7_s8-126",
        "Da_s8Da_u8_s8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_s8.da_u8_s8-127",
        "Da_s8Da_u9_s8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_s8.da_u9_s8-128",
        "Da_s8Da_u10_s8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_s8.da_u10_s8-129",
        "Da_s8Da_u11_s8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_s8.da_u11_s8-130",
        "Da_s8Da_u12_s8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_s8.da_u12_s8-131",
        "Da_s8Da_u13_s8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_s8.da_u13_s8-132",
        "Da_s8Da_u14_s8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_s8.da_u14_s8-133",
        "Da_s8Da_u15_s8": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_s8.da_u15_s8-134",
        "Da_s32Da_u0_s32": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_s32.da_u0_s32-135",
        "Da_s32Da_u1_s32": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_s32.da_u1_s32-136",
        "Da_s32Da_u2_s32": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_s32.da_u2_s32-137",
        "Da_s32Da_u3_s32": "ipv6SRv6Usid.header.dstAddrUSID.da_fmt.da_s32.da_u3_s32-138",
    }

    def __init__(self, parent, list_op=False):
        super(Ipv6SRv6Usid, self).__init__(parent, list_op)

    @property
    def VersionTCFLVersion(self):
        """
        Display Name: Version
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VersionTCFLVersion"])
        )

    @property
    def VersionTCFLTrafficClass(self):
        """
        Display Name: Traffic Class
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VersionTCFLTrafficClass"])
        )

    @property
    def VersionTCFLFlowLabel(self):
        """
        Display Name: Flow Label
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VersionTCFLFlowLabel"])
        )

    @property
    def HeaderPayloadLength(self):
        """
        Display Name: Payload Length
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderPayloadLength"])
        )

    @property
    def HeaderNextHeader(self):
        """
        Display Name: Next Header
        Default Value: 43
        Value Format: decimal
        Available enum values: HOPOPT, 0, IPv4 (Reduced encap - inner IPv4 directly), 4, TCP, 6, UDP (Reduced encap - e.g., RoCEv2 over UDP), 17, IPv6 (Reduced encap - inner IPv6 directly), 41, IPv6-Route (SRH present - standard SRv6), 43, IPv6-ICMP, 58, IPv6-NoNxt (Reduced, no inner payload), 59, Ethernet (Reduced encap - raw L2), 143, Experimental, 253, Reserved, 255
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderNextHeader"])
        )

    @property
    def HeaderHopLimit(self):
        """
        Display Name: Hop Limit
        Default Value: 255
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["HeaderHopLimit"])
        )

    @property
    def HeaderSrcIP(self):
        """
        Display Name: Source Address
        Default Value: 00::1
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HeaderSrcIP"]))

    @property
    def Da_fmtDa_full(self):
        """
        Display Name: Full IPv6 Address (128-bit)
        Default Value: 0
        Value Format: iPv6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Da_fmtDa_full"]))

    @property
    def Da_l16_0_16Lb_l16_0_16(self):
        """
        Display Name: Locator Block
        Default Value: 0x20010DB8
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l16_0_16Lb_l16_0_16"])
        )

    @property
    def Da_l16_0_16U0_l16_0_16(self):
        """
        Display Name: SID 0
        Default Value: 0x0001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l16_0_16U0_l16_0_16"])
        )

    @property
    def Da_l16_0_16U1_l16_0_16(self):
        """
        Display Name: SID 1
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l16_0_16U1_l16_0_16"])
        )

    @property
    def Da_l16_0_16U2_l16_0_16(self):
        """
        Display Name: SID 2
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l16_0_16U2_l16_0_16"])
        )

    @property
    def Da_l16_0_16U3_l16_0_16(self):
        """
        Display Name: SID 3
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l16_0_16U3_l16_0_16"])
        )

    @property
    def Da_l16_0_16U4_l16_0_16(self):
        """
        Display Name: SID 4
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l16_0_16U4_l16_0_16"])
        )

    @property
    def Da_l16_0_16U5_l16_0_16(self):
        """
        Display Name: SID 5
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l16_0_16U5_l16_0_16"])
        )

    @property
    def Da_l16_0_16U6_l16_0_16(self):
        """
        Display Name: EOM (End-of-Container)
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l16_0_16U6_l16_0_16"])
        )

    @property
    def Da_l32_16_16LocatorBlock(self):
        """
        Display Name: Locator Block
        Default Value: 0x20010DB8
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l32_16_16LocatorBlock"])
        )

    @property
    def Da_l32_16_16ActiveUSID(self):
        """
        Display Name: SID 0
        Default Value: 0x0001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l32_16_16ActiveUSID"])
        )

    @property
    def Da_l32_16_16NextUSID0(self):
        """
        Display Name: SID 1
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l32_16_16NextUSID0"])
        )

    @property
    def Da_l32_16_16NextUSID1(self):
        """
        Display Name: SID 2
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l32_16_16NextUSID1"])
        )

    @property
    def Da_l32_16_16NextUSID2(self):
        """
        Display Name: SID 3
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l32_16_16NextUSID2"])
        )

    @property
    def Da_l32_16_16NextUSID3(self):
        """
        Display Name: SID 4
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l32_16_16NextUSID3"])
        )

    @property
    def Da_l32_16_16EomUSID(self):
        """
        Display Name: EOM (End-of-Container)
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l32_16_16EomUSID"])
        )

    @property
    def Da_l48_16_16Lb_l48_16_16(self):
        """
        Display Name: Locator Block
        Default Value: 0x20010DB80001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l48_16_16Lb_l48_16_16"])
        )

    @property
    def Da_l48_16_16U0_l48_16_16(self):
        """
        Display Name: SID 0
        Default Value: 0x0001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l48_16_16U0_l48_16_16"])
        )

    @property
    def Da_l48_16_16U1_l48_16_16(self):
        """
        Display Name: SID 1
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l48_16_16U1_l48_16_16"])
        )

    @property
    def Da_l48_16_16U2_l48_16_16(self):
        """
        Display Name: SID 2
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l48_16_16U2_l48_16_16"])
        )

    @property
    def Da_l48_16_16U3_l48_16_16(self):
        """
        Display Name: SID 3
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l48_16_16U3_l48_16_16"])
        )

    @property
    def Da_l48_16_16U4_l48_16_16(self):
        """
        Display Name: EOM (End-of-Container)
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l48_16_16U4_l48_16_16"])
        )

    @property
    def Da_l64_0_16Lb_l64_0_16(self):
        """
        Display Name: Locator Block
        Default Value: 0x20010DB800000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l64_0_16Lb_l64_0_16"])
        )

    @property
    def Da_l64_0_16U0_l64_0_16(self):
        """
        Display Name: SID 0
        Default Value: 0x0001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l64_0_16U0_l64_0_16"])
        )

    @property
    def Da_l64_0_16U1_l64_0_16(self):
        """
        Display Name: SID 1
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l64_0_16U1_l64_0_16"])
        )

    @property
    def Da_l64_0_16U2_l64_0_16(self):
        """
        Display Name: SID 2
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l64_0_16U2_l64_0_16"])
        )

    @property
    def Da_l64_0_16U3_l64_0_16(self):
        """
        Display Name: EOM (End-of-Container)
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l64_0_16U3_l64_0_16"])
        )

    @property
    def Da_l80_0_16Lb_l80_0_16(self):
        """
        Display Name: Locator Block
        Default Value: 0x20010DB8000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l80_0_16Lb_l80_0_16"])
        )

    @property
    def Da_l80_0_16U0_l80_0_16(self):
        """
        Display Name: SID 0
        Default Value: 0x0001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l80_0_16U0_l80_0_16"])
        )

    @property
    def Da_l80_0_16U1_l80_0_16(self):
        """
        Display Name: SID 1
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l80_0_16U1_l80_0_16"])
        )

    @property
    def Da_l80_0_16U2_l80_0_16(self):
        """
        Display Name: EOM (End-of-Container)
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l80_0_16U2_l80_0_16"])
        )

    @property
    def Da_l96_0_16Lb_l96_0_16(self):
        """
        Display Name: Locator Block
        Default Value: 0x20010DB800000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l96_0_16Lb_l96_0_16"])
        )

    @property
    def Da_l96_0_16U0_l96_0_16(self):
        """
        Display Name: SID 0
        Default Value: 0x0001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l96_0_16U0_l96_0_16"])
        )

    @property
    def Da_l96_0_16U1_l96_0_16(self):
        """
        Display Name: EOM (End-of-Container)
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l96_0_16U1_l96_0_16"])
        )

    @property
    def Da_l16_0_8Lb_l16_0_8(self):
        """
        Display Name: Locator Block
        Default Value: 0x20010DB8
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l16_0_8Lb_l16_0_8"])
        )

    @property
    def Da_l16_0_8U0_l16_0_8(self):
        """
        Display Name: SID 0
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l16_0_8U0_l16_0_8"])
        )

    @property
    def Da_l16_0_8U1_l16_0_8(self):
        """
        Display Name: SID 1
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l16_0_8U1_l16_0_8"])
        )

    @property
    def Da_l16_0_8U2_l16_0_8(self):
        """
        Display Name: SID 2
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l16_0_8U2_l16_0_8"])
        )

    @property
    def Da_l16_0_8U3_l16_0_8(self):
        """
        Display Name: SID 3
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l16_0_8U3_l16_0_8"])
        )

    @property
    def Da_l16_0_8U4_l16_0_8(self):
        """
        Display Name: SID 4
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l16_0_8U4_l16_0_8"])
        )

    @property
    def Da_l16_0_8U5_l16_0_8(self):
        """
        Display Name: SID 5
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l16_0_8U5_l16_0_8"])
        )

    @property
    def Da_l16_0_8U6_l16_0_8(self):
        """
        Display Name: SID 6
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l16_0_8U6_l16_0_8"])
        )

    @property
    def Da_l16_0_8U7_l16_0_8(self):
        """
        Display Name: SID 7
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l16_0_8U7_l16_0_8"])
        )

    @property
    def Da_l16_0_8U8_l16_0_8(self):
        """
        Display Name: SID 8
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l16_0_8U8_l16_0_8"])
        )

    @property
    def Da_l16_0_8U9_l16_0_8(self):
        """
        Display Name: SID 9
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l16_0_8U9_l16_0_8"])
        )

    @property
    def Da_l16_0_8U10_l16_0_8(self):
        """
        Display Name: SID 10
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l16_0_8U10_l16_0_8"])
        )

    @property
    def Da_l16_0_8U11_l16_0_8(self):
        """
        Display Name: SID 11
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l16_0_8U11_l16_0_8"])
        )

    @property
    def Da_l16_0_8U12_l16_0_8(self):
        """
        Display Name: SID 12
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l16_0_8U12_l16_0_8"])
        )

    @property
    def Da_l16_0_8U13_l16_0_8(self):
        """
        Display Name: EOM (End-of-Container)
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l16_0_8U13_l16_0_8"])
        )

    @property
    def Da_l32_16_8Lb_l32_16_8(self):
        """
        Display Name: Locator Block
        Default Value: 0x20010DB8
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l32_16_8Lb_l32_16_8"])
        )

    @property
    def Da_l32_16_8U0_l32_16_8(self):
        """
        Display Name: SID 0
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l32_16_8U0_l32_16_8"])
        )

    @property
    def Da_l32_16_8U1_l32_16_8(self):
        """
        Display Name: SID 1
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l32_16_8U1_l32_16_8"])
        )

    @property
    def Da_l32_16_8U2_l32_16_8(self):
        """
        Display Name: SID 2
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l32_16_8U2_l32_16_8"])
        )

    @property
    def Da_l32_16_8U3_l32_16_8(self):
        """
        Display Name: SID 3
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l32_16_8U3_l32_16_8"])
        )

    @property
    def Da_l32_16_8U4_l32_16_8(self):
        """
        Display Name: SID 4
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l32_16_8U4_l32_16_8"])
        )

    @property
    def Da_l32_16_8U5_l32_16_8(self):
        """
        Display Name: SID 5
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l32_16_8U5_l32_16_8"])
        )

    @property
    def Da_l32_16_8U6_l32_16_8(self):
        """
        Display Name: SID 6
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l32_16_8U6_l32_16_8"])
        )

    @property
    def Da_l32_16_8U7_l32_16_8(self):
        """
        Display Name: SID 7
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l32_16_8U7_l32_16_8"])
        )

    @property
    def Da_l32_16_8U8_l32_16_8(self):
        """
        Display Name: SID 8
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l32_16_8U8_l32_16_8"])
        )

    @property
    def Da_l32_16_8U9_l32_16_8(self):
        """
        Display Name: SID 9
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l32_16_8U9_l32_16_8"])
        )

    @property
    def Da_l32_16_8U10_l32_16_8(self):
        """
        Display Name: SID 10
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l32_16_8U10_l32_16_8"])
        )

    @property
    def Da_l32_16_8U11_l32_16_8(self):
        """
        Display Name: EOM (End-of-Container)
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l32_16_8U11_l32_16_8"])
        )

    @property
    def Da_l48_0_8Lb_l48_0_8(self):
        """
        Display Name: Locator Block
        Default Value: 0x20010DB80001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l48_0_8Lb_l48_0_8"])
        )

    @property
    def Da_l48_0_8U0_l48_0_8(self):
        """
        Display Name: SID 0
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l48_0_8U0_l48_0_8"])
        )

    @property
    def Da_l48_0_8U1_l48_0_8(self):
        """
        Display Name: SID 1
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l48_0_8U1_l48_0_8"])
        )

    @property
    def Da_l48_0_8U2_l48_0_8(self):
        """
        Display Name: SID 2
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l48_0_8U2_l48_0_8"])
        )

    @property
    def Da_l48_0_8U3_l48_0_8(self):
        """
        Display Name: SID 3
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l48_0_8U3_l48_0_8"])
        )

    @property
    def Da_l48_0_8U4_l48_0_8(self):
        """
        Display Name: SID 4
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l48_0_8U4_l48_0_8"])
        )

    @property
    def Da_l48_0_8U5_l48_0_8(self):
        """
        Display Name: SID 5
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l48_0_8U5_l48_0_8"])
        )

    @property
    def Da_l48_0_8U6_l48_0_8(self):
        """
        Display Name: SID 6
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l48_0_8U6_l48_0_8"])
        )

    @property
    def Da_l48_0_8U7_l48_0_8(self):
        """
        Display Name: SID 7
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l48_0_8U7_l48_0_8"])
        )

    @property
    def Da_l48_0_8U8_l48_0_8(self):
        """
        Display Name: SID 8
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l48_0_8U8_l48_0_8"])
        )

    @property
    def Da_l48_0_8U9_l48_0_8(self):
        """
        Display Name: EOM (End-of-Container)
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l48_0_8U9_l48_0_8"])
        )

    @property
    def Da_l64_0_8Lb_l64_0_8(self):
        """
        Display Name: Locator Block
        Default Value: 0x20010DB800000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l64_0_8Lb_l64_0_8"])
        )

    @property
    def Da_l64_0_8U0_l64_0_8(self):
        """
        Display Name: SID 0
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l64_0_8U0_l64_0_8"])
        )

    @property
    def Da_l64_0_8U1_l64_0_8(self):
        """
        Display Name: SID 1
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l64_0_8U1_l64_0_8"])
        )

    @property
    def Da_l64_0_8U2_l64_0_8(self):
        """
        Display Name: SID 2
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l64_0_8U2_l64_0_8"])
        )

    @property
    def Da_l64_0_8U3_l64_0_8(self):
        """
        Display Name: SID 3
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l64_0_8U3_l64_0_8"])
        )

    @property
    def Da_l64_0_8U4_l64_0_8(self):
        """
        Display Name: SID 4
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l64_0_8U4_l64_0_8"])
        )

    @property
    def Da_l64_0_8U5_l64_0_8(self):
        """
        Display Name: SID 5
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l64_0_8U5_l64_0_8"])
        )

    @property
    def Da_l64_0_8U6_l64_0_8(self):
        """
        Display Name: SID 6
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l64_0_8U6_l64_0_8"])
        )

    @property
    def Da_l64_0_8U7_l64_0_8(self):
        """
        Display Name: EOM (End-of-Container)
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l64_0_8U7_l64_0_8"])
        )

    @property
    def Da_l80_0_8Lb_l80_0_8(self):
        """
        Display Name: Locator Block
        Default Value: 0x20010DB8000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l80_0_8Lb_l80_0_8"])
        )

    @property
    def Da_l80_0_8U0_l80_0_8(self):
        """
        Display Name: SID 0
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l80_0_8U0_l80_0_8"])
        )

    @property
    def Da_l80_0_8U1_l80_0_8(self):
        """
        Display Name: SID 1
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l80_0_8U1_l80_0_8"])
        )

    @property
    def Da_l80_0_8U2_l80_0_8(self):
        """
        Display Name: SID 2
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l80_0_8U2_l80_0_8"])
        )

    @property
    def Da_l80_0_8U3_l80_0_8(self):
        """
        Display Name: SID 3
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l80_0_8U3_l80_0_8"])
        )

    @property
    def Da_l80_0_8U4_l80_0_8(self):
        """
        Display Name: SID 4
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l80_0_8U4_l80_0_8"])
        )

    @property
    def Da_l80_0_8U5_l80_0_8(self):
        """
        Display Name: EOM (End-of-Container)
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l80_0_8U5_l80_0_8"])
        )

    @property
    def Da_l96_0_8Lb_l96_0_8(self):
        """
        Display Name: Locator Block
        Default Value: 0x20010DB800000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l96_0_8Lb_l96_0_8"])
        )

    @property
    def Da_l96_0_8U0_l96_0_8(self):
        """
        Display Name: SID 0
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l96_0_8U0_l96_0_8"])
        )

    @property
    def Da_l96_0_8U1_l96_0_8(self):
        """
        Display Name: SID 1
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l96_0_8U1_l96_0_8"])
        )

    @property
    def Da_l96_0_8U2_l96_0_8(self):
        """
        Display Name: SID 2
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l96_0_8U2_l96_0_8"])
        )

    @property
    def Da_l96_0_8U3_l96_0_8(self):
        """
        Display Name: EOM (End-of-Container)
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l96_0_8U3_l96_0_8"])
        )

    @property
    def Da_l32_0_32Lb_l32_0_32(self):
        """
        Display Name: Locator Block
        Default Value: 0x20010DB8
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l32_0_32Lb_l32_0_32"])
        )

    @property
    def Da_l32_0_32U0_l32_0_32(self):
        """
        Display Name: SID 0
        Default Value: 0x00000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l32_0_32U0_l32_0_32"])
        )

    @property
    def Da_l32_0_32U1_l32_0_32(self):
        """
        Display Name: SID 1
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l32_0_32U1_l32_0_32"])
        )

    @property
    def Da_l32_0_32U2_l32_0_32(self):
        """
        Display Name: EOM (End-of-Container)
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l32_0_32U2_l32_0_32"])
        )

    @property
    def Da_l64_0_32Lb_l64_0_32(self):
        """
        Display Name: Locator Block
        Default Value: 0x20010DB800000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l64_0_32Lb_l64_0_32"])
        )

    @property
    def Da_l64_0_32U0_l64_0_32(self):
        """
        Display Name: SID 0
        Default Value: 0x00000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l64_0_32U0_l64_0_32"])
        )

    @property
    def Da_l64_0_32U1_l64_0_32(self):
        """
        Display Name: EOM (End-of-Container)
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l64_0_32U1_l64_0_32"])
        )

    @property
    def Da_l96_0_32Lb_l96_0_32(self):
        """
        Display Name: Locator Block
        Default Value: 0x20010DB800000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l96_0_32Lb_l96_0_32"])
        )

    @property
    def Da_l96_0_32U0_l96_0_32(self):
        """
        Display Name: SID 0
        Default Value: 0x00000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_l96_0_32U0_l96_0_32"])
        )

    @property
    def Da_s16Da_u0_s16(self):
        """
        Display Name: uSID 0
        Default Value: 0x0001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_s16Da_u0_s16"])
        )

    @property
    def Da_s16Da_u1_s16(self):
        """
        Display Name: uSID 1
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_s16Da_u1_s16"])
        )

    @property
    def Da_s16Da_u2_s16(self):
        """
        Display Name: uSID 2
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_s16Da_u2_s16"])
        )

    @property
    def Da_s16Da_u3_s16(self):
        """
        Display Name: uSID 3
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_s16Da_u3_s16"])
        )

    @property
    def Da_s16Da_u4_s16(self):
        """
        Display Name: uSID 4
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_s16Da_u4_s16"])
        )

    @property
    def Da_s16Da_u5_s16(self):
        """
        Display Name: uSID 5
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_s16Da_u5_s16"])
        )

    @property
    def Da_s16Da_u6_s16(self):
        """
        Display Name: uSID 6
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_s16Da_u6_s16"])
        )

    @property
    def Da_s16Da_u7_s16(self):
        """
        Display Name: uSID 7
        Default Value: 0x0000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_s16Da_u7_s16"])
        )

    @property
    def Da_s8Da_u0_s8(self):
        """
        Display Name: uSID 0
        Default Value: 0x01
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Da_s8Da_u0_s8"]))

    @property
    def Da_s8Da_u1_s8(self):
        """
        Display Name: uSID 1
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Da_s8Da_u1_s8"]))

    @property
    def Da_s8Da_u2_s8(self):
        """
        Display Name: uSID 2
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Da_s8Da_u2_s8"]))

    @property
    def Da_s8Da_u3_s8(self):
        """
        Display Name: uSID 3
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Da_s8Da_u3_s8"]))

    @property
    def Da_s8Da_u4_s8(self):
        """
        Display Name: uSID 4
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Da_s8Da_u4_s8"]))

    @property
    def Da_s8Da_u5_s8(self):
        """
        Display Name: uSID 5
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Da_s8Da_u5_s8"]))

    @property
    def Da_s8Da_u6_s8(self):
        """
        Display Name: uSID 6
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Da_s8Da_u6_s8"]))

    @property
    def Da_s8Da_u7_s8(self):
        """
        Display Name: uSID 7
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Da_s8Da_u7_s8"]))

    @property
    def Da_s8Da_u8_s8(self):
        """
        Display Name: uSID 8
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Da_s8Da_u8_s8"]))

    @property
    def Da_s8Da_u9_s8(self):
        """
        Display Name: uSID 9
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Da_s8Da_u9_s8"]))

    @property
    def Da_s8Da_u10_s8(self):
        """
        Display Name: uSID 10
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_s8Da_u10_s8"])
        )

    @property
    def Da_s8Da_u11_s8(self):
        """
        Display Name: uSID 11
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_s8Da_u11_s8"])
        )

    @property
    def Da_s8Da_u12_s8(self):
        """
        Display Name: uSID 12
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_s8Da_u12_s8"])
        )

    @property
    def Da_s8Da_u13_s8(self):
        """
        Display Name: uSID 13
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_s8Da_u13_s8"])
        )

    @property
    def Da_s8Da_u14_s8(self):
        """
        Display Name: uSID 14
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_s8Da_u14_s8"])
        )

    @property
    def Da_s8Da_u15_s8(self):
        """
        Display Name: uSID 15
        Default Value: 0x00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_s8Da_u15_s8"])
        )

    @property
    def Da_s32Da_u0_s32(self):
        """
        Display Name: uSID 0
        Default Value: 0x00000001
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_s32Da_u0_s32"])
        )

    @property
    def Da_s32Da_u1_s32(self):
        """
        Display Name: uSID 1
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_s32Da_u1_s32"])
        )

    @property
    def Da_s32Da_u2_s32(self):
        """
        Display Name: uSID 2
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_s32Da_u2_s32"])
        )

    @property
    def Da_s32Da_u3_s32(self):
        """
        Display Name: uSID 3
        Default Value: 0x00000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["Da_s32Da_u3_s32"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
