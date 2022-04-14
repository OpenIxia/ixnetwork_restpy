from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Bier(Base):
    __slots__ = ()
    _SDM_NAME = "bier"
    _SDM_ATT_MAP = {
        "Nibble": "bier.header.nibble-1",
        "Ver": "bier.header.ver-2",
        "Bsl": "bier.header.bsl-3",
        "Entropy": "bier.header.entropy-4",
        "Oam": "bier.header.oam-5",
        "Rsv": "bier.header.rsv-6",
        "Dscp": "bier.header.dscp-7",
        "Proto": "bier.header.proto-8",
        "BfirId": "bier.header.bfirId-9",
        "BitStringEgressPeerSet0": "bier.header.bitString.egressPeerSet0-10",
        "BitStringEgressPeerSet1": "bier.header.bitString.egressPeerSet1-11",
        "BitStringEgressPeerSet2": "bier.header.bitString.egressPeerSet2-12",
        "BitStringEgressPeerSet3": "bier.header.bitString.egressPeerSet3-13",
        "BitStringEgressPeerSet4": "bier.header.bitString.egressPeerSet4-14",
        "BitStringEgressPeerSet5": "bier.header.bitString.egressPeerSet5-15",
        "BitStringEgressPeerSet6": "bier.header.bitString.egressPeerSet6-16",
        "BitStringEgressPeerSet7": "bier.header.bitString.egressPeerSet7-17",
        "BitStringEgressPeerSet8": "bier.header.bitString.egressPeerSet8-18",
        "BitStringEgressPeerSet9": "bier.header.bitString.egressPeerSet9-19",
        "BitStringEgressPeerSet10": "bier.header.bitString.egressPeerSet10-20",
        "BitStringEgressPeerSet11": "bier.header.bitString.egressPeerSet11-21",
        "BitStringEgressPeerSet12": "bier.header.bitString.egressPeerSet12-22",
        "BitStringEgressPeerSet13": "bier.header.bitString.egressPeerSet13-23",
        "BitStringEgressPeerSet14": "bier.header.bitString.egressPeerSet14-24",
        "BitStringEgressPeerSet15": "bier.header.bitString.egressPeerSet15-25",
        "BitStringEgressPeerSet16": "bier.header.bitString.egressPeerSet16-26",
        "BitStringEgressPeerSet17": "bier.header.bitString.egressPeerSet17-27",
        "BitStringEgressPeerSet18": "bier.header.bitString.egressPeerSet18-28",
        "BitStringEgressPeerSet19": "bier.header.bitString.egressPeerSet19-29",
        "BitStringEgressPeerSet20": "bier.header.bitString.egressPeerSet20-30",
        "BitStringEgressPeerSet21": "bier.header.bitString.egressPeerSet21-31",
        "BitStringEgressPeerSet22": "bier.header.bitString.egressPeerSet22-32",
        "BitStringEgressPeerSet23": "bier.header.bitString.egressPeerSet23-33",
        "BitStringEgressPeerSet24": "bier.header.bitString.egressPeerSet24-34",
        "BitStringEgressPeerSet25": "bier.header.bitString.egressPeerSet25-35",
        "BitStringEgressPeerSet26": "bier.header.bitString.egressPeerSet26-36",
        "BitStringEgressPeerSet27": "bier.header.bitString.egressPeerSet27-37",
        "BitStringEgressPeerSet28": "bier.header.bitString.egressPeerSet28-38",
        "BitStringEgressPeerSet29": "bier.header.bitString.egressPeerSet29-39",
        "BitStringEgressPeerSet30": "bier.header.bitString.egressPeerSet30-40",
        "BitStringEgressPeerSet31": "bier.header.bitString.egressPeerSet31-41",
        "BitStringEgressPeerSet32": "bier.header.bitString.egressPeerSet32-42",
        "BitStringEgressPeerSet33": "bier.header.bitString.egressPeerSet33-43",
        "BitStringEgressPeerSet34": "bier.header.bitString.egressPeerSet34-44",
        "BitStringEgressPeerSet35": "bier.header.bitString.egressPeerSet35-45",
        "BitStringEgressPeerSet36": "bier.header.bitString.egressPeerSet36-46",
        "BitStringEgressPeerSet37": "bier.header.bitString.egressPeerSet37-47",
        "BitStringEgressPeerSet38": "bier.header.bitString.egressPeerSet38-48",
        "BitStringEgressPeerSet39": "bier.header.bitString.egressPeerSet39-49",
        "BitStringEgressPeerSet40": "bier.header.bitString.egressPeerSet40-50",
        "BitStringEgressPeerSet41": "bier.header.bitString.egressPeerSet41-51",
        "BitStringEgressPeerSet42": "bier.header.bitString.egressPeerSet42-52",
        "BitStringEgressPeerSet43": "bier.header.bitString.egressPeerSet43-53",
        "BitStringEgressPeerSet44": "bier.header.bitString.egressPeerSet44-54",
        "BitStringEgressPeerSet45": "bier.header.bitString.egressPeerSet45-55",
        "BitStringEgressPeerSet46": "bier.header.bitString.egressPeerSet46-56",
        "BitStringEgressPeerSet47": "bier.header.bitString.egressPeerSet47-57",
        "BitStringEgressPeerSet48": "bier.header.bitString.egressPeerSet48-58",
        "BitStringEgressPeerSet49": "bier.header.bitString.egressPeerSet49-59",
        "BitStringEgressPeerSet50": "bier.header.bitString.egressPeerSet50-60",
        "BitStringEgressPeerSet51": "bier.header.bitString.egressPeerSet51-61",
        "BitStringEgressPeerSet52": "bier.header.bitString.egressPeerSet52-62",
        "BitStringEgressPeerSet53": "bier.header.bitString.egressPeerSet53-63",
        "BitStringEgressPeerSet54": "bier.header.bitString.egressPeerSet54-64",
        "BitStringEgressPeerSet55": "bier.header.bitString.egressPeerSet55-65",
        "BitStringEgressPeerSet56": "bier.header.bitString.egressPeerSet56-66",
        "BitStringEgressPeerSet57": "bier.header.bitString.egressPeerSet57-67",
        "BitStringEgressPeerSet58": "bier.header.bitString.egressPeerSet58-68",
        "BitStringEgressPeerSet59": "bier.header.bitString.egressPeerSet59-69",
        "BitStringEgressPeerSet60": "bier.header.bitString.egressPeerSet60-70",
        "BitStringEgressPeerSet61": "bier.header.bitString.egressPeerSet61-71",
        "BitStringEgressPeerSet62": "bier.header.bitString.egressPeerSet62-72",
        "BitStringEgressPeerSet63": "bier.header.bitString.egressPeerSet63-73",
    }

    def __init__(self, parent, list_op=False):
        super(Bier, self).__init__(parent, list_op)

    @property
    def Nibble(self):
        """
        Display Name: Nibble
        Default Value: 5
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Nibble"]))

    @property
    def Ver(self):
        """
        Display Name: Ver
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Ver"]))

    @property
    def Bsl(self):
        """
        Display Name: BSL
        Default Value: 3
        Value Format: decimal
        Available enum values: Not Supported, 0, 64 Bits, 1, 128 Bits, 2, 256 Bits, 3, 512 Bits, 4, 1024 Bits, 5, 2048 Bits, 6, 4096 Bits, 7
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Bsl"]))

    @property
    def Entropy(self):
        """
        Display Name: Entropy
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Entropy"]))

    @property
    def Oam(self):
        """
        Display Name: OAM
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Oam"]))

    @property
    def Rsv(self):
        """
        Display Name: Rsv
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Rsv"]))

    @property
    def Dscp(self):
        """
        Display Name: DSCP
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Dscp"]))

    @property
    def Proto(self):
        """
        Display Name: Proto
        Default Value: 2
        Value Format: decimal
        Available enum values: Reserved, 0, MPLS Packet W/ Downstream-Assigned Label at Top of Stack, 1, MPLS Packet W/ Upstream-Assigned Label at Top of Stack, 2, Ethernet Frame, 3, IPv4 Packet, 4, OAM Packet, 5, IPv6 Packet, 6
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Proto"]))

    @property
    def BfirId(self):
        """
        Display Name: BFIR-Id
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BfirId"]))

    @property
    def BitStringEgressPeerSet0(self):
        """
        Display Name: Egress Peer Set 0
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet0"])
        )

    @property
    def BitStringEgressPeerSet1(self):
        """
        Display Name: Egress Peer Set 1
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet1"])
        )

    @property
    def BitStringEgressPeerSet2(self):
        """
        Display Name: Egress Peer Set 2
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet2"])
        )

    @property
    def BitStringEgressPeerSet3(self):
        """
        Display Name: Egress Peer Set 3
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet3"])
        )

    @property
    def BitStringEgressPeerSet4(self):
        """
        Display Name: Egress Peer Set 4
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet4"])
        )

    @property
    def BitStringEgressPeerSet5(self):
        """
        Display Name: Egress Peer Set 5
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet5"])
        )

    @property
    def BitStringEgressPeerSet6(self):
        """
        Display Name: Egress Peer Set 6
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet6"])
        )

    @property
    def BitStringEgressPeerSet7(self):
        """
        Display Name: Egress Peer Set 7
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet7"])
        )

    @property
    def BitStringEgressPeerSet8(self):
        """
        Display Name: Egress Peer Set 8
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet8"])
        )

    @property
    def BitStringEgressPeerSet9(self):
        """
        Display Name: Egress Peer Set 9
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet9"])
        )

    @property
    def BitStringEgressPeerSet10(self):
        """
        Display Name: Egress Peer Set 10
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet10"])
        )

    @property
    def BitStringEgressPeerSet11(self):
        """
        Display Name: Egress Peer Set 11
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet11"])
        )

    @property
    def BitStringEgressPeerSet12(self):
        """
        Display Name: Egress Peer Set 12
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet12"])
        )

    @property
    def BitStringEgressPeerSet13(self):
        """
        Display Name: Egress Peer Set 13
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet13"])
        )

    @property
    def BitStringEgressPeerSet14(self):
        """
        Display Name: Egress Peer Set 14
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet14"])
        )

    @property
    def BitStringEgressPeerSet15(self):
        """
        Display Name: Egress Peer Set 15
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet15"])
        )

    @property
    def BitStringEgressPeerSet16(self):
        """
        Display Name: Egress Peer Set 16
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet16"])
        )

    @property
    def BitStringEgressPeerSet17(self):
        """
        Display Name: Egress Peer Set 17
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet17"])
        )

    @property
    def BitStringEgressPeerSet18(self):
        """
        Display Name: Egress Peer Set 18
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet18"])
        )

    @property
    def BitStringEgressPeerSet19(self):
        """
        Display Name: Egress Peer Set 19
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet19"])
        )

    @property
    def BitStringEgressPeerSet20(self):
        """
        Display Name: Egress Peer Set 20
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet20"])
        )

    @property
    def BitStringEgressPeerSet21(self):
        """
        Display Name: Egress Peer Set 21
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet21"])
        )

    @property
    def BitStringEgressPeerSet22(self):
        """
        Display Name: Egress Peer Set 22
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet22"])
        )

    @property
    def BitStringEgressPeerSet23(self):
        """
        Display Name: Egress Peer Set 23
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet23"])
        )

    @property
    def BitStringEgressPeerSet24(self):
        """
        Display Name: Egress Peer Set 24
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet24"])
        )

    @property
    def BitStringEgressPeerSet25(self):
        """
        Display Name: Egress Peer Set 25
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet25"])
        )

    @property
    def BitStringEgressPeerSet26(self):
        """
        Display Name: Egress Peer Set 26
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet26"])
        )

    @property
    def BitStringEgressPeerSet27(self):
        """
        Display Name: Egress Peer Set 27
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet27"])
        )

    @property
    def BitStringEgressPeerSet28(self):
        """
        Display Name: Egress Peer Set 28
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet28"])
        )

    @property
    def BitStringEgressPeerSet29(self):
        """
        Display Name: Egress Peer Set 29
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet29"])
        )

    @property
    def BitStringEgressPeerSet30(self):
        """
        Display Name: Egress Peer Set 30
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet30"])
        )

    @property
    def BitStringEgressPeerSet31(self):
        """
        Display Name: Egress Peer Set 31
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet31"])
        )

    @property
    def BitStringEgressPeerSet32(self):
        """
        Display Name: Egress Peer Set 32
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet32"])
        )

    @property
    def BitStringEgressPeerSet33(self):
        """
        Display Name: Egress Peer Set 33
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet33"])
        )

    @property
    def BitStringEgressPeerSet34(self):
        """
        Display Name: Egress Peer Set 34
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet34"])
        )

    @property
    def BitStringEgressPeerSet35(self):
        """
        Display Name: Egress Peer Set 35
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet35"])
        )

    @property
    def BitStringEgressPeerSet36(self):
        """
        Display Name: Egress Peer Set 36
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet36"])
        )

    @property
    def BitStringEgressPeerSet37(self):
        """
        Display Name: Egress Peer Set 37
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet37"])
        )

    @property
    def BitStringEgressPeerSet38(self):
        """
        Display Name: Egress Peer Set 38
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet38"])
        )

    @property
    def BitStringEgressPeerSet39(self):
        """
        Display Name: Egress Peer Set 39
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet39"])
        )

    @property
    def BitStringEgressPeerSet40(self):
        """
        Display Name: Egress Peer Set 40
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet40"])
        )

    @property
    def BitStringEgressPeerSet41(self):
        """
        Display Name: Egress Peer Set 41
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet41"])
        )

    @property
    def BitStringEgressPeerSet42(self):
        """
        Display Name: Egress Peer Set 42
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet42"])
        )

    @property
    def BitStringEgressPeerSet43(self):
        """
        Display Name: Egress Peer Set 43
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet43"])
        )

    @property
    def BitStringEgressPeerSet44(self):
        """
        Display Name: Egress Peer Set 44
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet44"])
        )

    @property
    def BitStringEgressPeerSet45(self):
        """
        Display Name: Egress Peer Set 45
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet45"])
        )

    @property
    def BitStringEgressPeerSet46(self):
        """
        Display Name: Egress Peer Set 46
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet46"])
        )

    @property
    def BitStringEgressPeerSet47(self):
        """
        Display Name: Egress Peer Set 47
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet47"])
        )

    @property
    def BitStringEgressPeerSet48(self):
        """
        Display Name: Egress Peer Set 48
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet48"])
        )

    @property
    def BitStringEgressPeerSet49(self):
        """
        Display Name: Egress Peer Set 49
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet49"])
        )

    @property
    def BitStringEgressPeerSet50(self):
        """
        Display Name: Egress Peer Set 50
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet50"])
        )

    @property
    def BitStringEgressPeerSet51(self):
        """
        Display Name: Egress Peer Set 51
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet51"])
        )

    @property
    def BitStringEgressPeerSet52(self):
        """
        Display Name: Egress Peer Set 52
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet52"])
        )

    @property
    def BitStringEgressPeerSet53(self):
        """
        Display Name: Egress Peer Set 53
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet53"])
        )

    @property
    def BitStringEgressPeerSet54(self):
        """
        Display Name: Egress Peer Set 54
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet54"])
        )

    @property
    def BitStringEgressPeerSet55(self):
        """
        Display Name: Egress Peer Set 55
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet55"])
        )

    @property
    def BitStringEgressPeerSet56(self):
        """
        Display Name: Egress Peer Set 56
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet56"])
        )

    @property
    def BitStringEgressPeerSet57(self):
        """
        Display Name: Egress Peer Set 57
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet57"])
        )

    @property
    def BitStringEgressPeerSet58(self):
        """
        Display Name: Egress Peer Set 58
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet58"])
        )

    @property
    def BitStringEgressPeerSet59(self):
        """
        Display Name: Egress Peer Set 59
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet59"])
        )

    @property
    def BitStringEgressPeerSet60(self):
        """
        Display Name: Egress Peer Set 60
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet60"])
        )

    @property
    def BitStringEgressPeerSet61(self):
        """
        Display Name: Egress Peer Set 61
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet61"])
        )

    @property
    def BitStringEgressPeerSet62(self):
        """
        Display Name: Egress Peer Set 62
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet62"])
        )

    @property
    def BitStringEgressPeerSet63(self):
        """
        Display Name: Egress Peer Set 63
        Default Value: 0x0000000000000000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["BitStringEgressPeerSet63"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
