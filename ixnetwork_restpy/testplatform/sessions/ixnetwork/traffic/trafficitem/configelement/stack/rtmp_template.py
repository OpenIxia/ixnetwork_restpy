from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class Rtmp(Base):
    __slots__ = ()
    _SDM_NAME = "rtmp "
    _SDM_ATT_MAP = {
        "RtmpNonextendedNetworkNumber": "rtmp .header.messageType.rtmpNonextended.networkNumber-1",
        "RtmpNonextendedNodeIDLength": "rtmp .header.messageType.rtmpNonextended.nodeIDLength-2",
        "RtmpNonextendedRouterNodeId": "rtmp .header.messageType.rtmpNonextended.routerNodeId-3",
        "RtmpNonextendedUnused": "rtmp .header.messageType.rtmpNonextended.unused-4",
        "RtmpNonextendedVersion": "rtmp .header.messageType.rtmpNonextended.version-5",
        "RoutingTupleNonextendedNetworkNumber": "rtmp .header.messageType.rtmpNonextended.nextRoutingTuple.routingTuple.routingTupleNonextended.networkNumber-6",
        "RoutingTupleNonextendedRangeFlag": "rtmp .header.messageType.rtmpNonextended.nextRoutingTuple.routingTuple.routingTupleNonextended.rangeFlag-7",
        "RoutingTupleNonextendedReserved": "rtmp .header.messageType.rtmpNonextended.nextRoutingTuple.routingTuple.routingTupleNonextended.reserved-8",
        "RoutingTupleNonextendedDistance": "rtmp .header.messageType.rtmpNonextended.nextRoutingTuple.routingTuple.routingTupleNonextended.distance-9",
        "RoutingTupleExtendedRangeStart": "rtmp .header.messageType.rtmpNonextended.nextRoutingTuple.routingTuple.routingTupleExtended.rangeStart-10",
        "RoutingTupleExtendedRangeFlag": "rtmp .header.messageType.rtmpNonextended.nextRoutingTuple.routingTuple.routingTupleExtended.rangeFlag-11",
        "RoutingTupleExtendedReserved": "rtmp .header.messageType.rtmpNonextended.nextRoutingTuple.routingTuple.routingTupleExtended.reserved-12",
        "RoutingTupleExtendedDistance": "rtmp .header.messageType.rtmpNonextended.nextRoutingTuple.routingTuple.routingTupleExtended.distance-13",
        "RoutingTupleExtendedRangeEnd": "rtmp .header.messageType.rtmpNonextended.nextRoutingTuple.routingTuple.routingTupleExtended.rangeEnd-14",
        "RoutingTupleExtendedVersion": "rtmp .header.messageType.rtmpNonextended.nextRoutingTuple.routingTuple.routingTupleExtended.version-15",
        "RtmpExtendedNetworkNumber": "rtmp .header.messageType.rtmpExtended.networkNumber-16",
        "RtmpExtendedNodeIDLength": "rtmp .header.messageType.rtmpExtended.nodeIDLength-17",
        "RtmpExtendedRouterNodeId": "rtmp .header.messageType.rtmpExtended.routerNodeId-18",
        "RoutingtupleRoutingTupleNonextendedNetworkNumber": "rtmp .header.messageType.rtmpExtended.nextRoutingTuple.routingTuple.routingTupleNonextended.networkNumber-19",
        "RoutingtupleRoutingTupleNonextendedRangeFlag": "rtmp .header.messageType.rtmpExtended.nextRoutingTuple.routingTuple.routingTupleNonextended.rangeFlag-20",
        "RoutingtupleRoutingTupleNonextendedReserved": "rtmp .header.messageType.rtmpExtended.nextRoutingTuple.routingTuple.routingTupleNonextended.reserved-21",
        "RoutingtupleRoutingTupleNonextendedDistance": "rtmp .header.messageType.rtmpExtended.nextRoutingTuple.routingTuple.routingTupleNonextended.distance-22",
        "RoutingtupleRoutingTupleExtendedRangeStart": "rtmp .header.messageType.rtmpExtended.nextRoutingTuple.routingTuple.routingTupleExtended.rangeStart-23",
        "RoutingtupleRoutingTupleExtendedRangeFlag": "rtmp .header.messageType.rtmpExtended.nextRoutingTuple.routingTuple.routingTupleExtended.rangeFlag-24",
        "RoutingtupleRoutingTupleExtendedReserved": "rtmp .header.messageType.rtmpExtended.nextRoutingTuple.routingTuple.routingTupleExtended.reserved-25",
        "RoutingtupleRoutingTupleExtendedDistance": "rtmp .header.messageType.rtmpExtended.nextRoutingTuple.routingTuple.routingTupleExtended.distance-26",
        "RoutingtupleRoutingTupleExtendedRangeEnd": "rtmp .header.messageType.rtmpExtended.nextRoutingTuple.routingTuple.routingTupleExtended.rangeEnd-27",
        "RoutingtupleRoutingTupleExtendedVersion": "rtmp .header.messageType.rtmpExtended.nextRoutingTuple.routingTuple.routingTupleExtended.version-28",
    }

    def __init__(self, parent, list_op=False):
        super(Rtmp, self).__init__(parent, list_op)

    @property
    def RtmpNonextendedNetworkNumber(self):
        """
        Display Name: Router's Network Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RtmpNonextendedNetworkNumber"])
        )

    @property
    def RtmpNonextendedNodeIDLength(self):
        """
        Display Name: Node ID length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RtmpNonextendedNodeIDLength"])
        )

    @property
    def RtmpNonextendedRouterNodeId(self):
        """
        Display Name: Router's Node ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RtmpNonextendedRouterNodeId"])
        )

    @property
    def RtmpNonextendedUnused(self):
        """
        Display Name: Unused
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RtmpNonextendedUnused"])
        )

    @property
    def RtmpNonextendedVersion(self):
        """
        Display Name: Version
        Default Value: 0x82
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RtmpNonextendedVersion"])
        )

    @property
    def RoutingTupleNonextendedNetworkNumber(self):
        """
        Display Name: Network Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RoutingTupleNonextendedNetworkNumber"]
            ),
        )

    @property
    def RoutingTupleNonextendedRangeFlag(self):
        """
        Display Name: Range Flag
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RoutingTupleNonextendedRangeFlag"]),
        )

    @property
    def RoutingTupleNonextendedReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RoutingTupleNonextendedReserved"]),
        )

    @property
    def RoutingTupleNonextendedDistance(self):
        """
        Display Name: Distance
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RoutingTupleNonextendedDistance"]),
        )

    @property
    def RoutingTupleExtendedRangeStart(self):
        """
        Display Name: Range Start
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RoutingTupleExtendedRangeStart"]),
        )

    @property
    def RoutingTupleExtendedRangeFlag(self):
        """
        Display Name: Range Flag
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["RoutingTupleExtendedRangeFlag"]),
        )

    @property
    def RoutingTupleExtendedReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RoutingTupleExtendedReserved"])
        )

    @property
    def RoutingTupleExtendedDistance(self):
        """
        Display Name: Distance
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RoutingTupleExtendedDistance"])
        )

    @property
    def RoutingTupleExtendedRangeEnd(self):
        """
        Display Name: Range End
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RoutingTupleExtendedRangeEnd"])
        )

    @property
    def RoutingTupleExtendedVersion(self):
        """
        Display Name: Version
        Default Value: 0x82
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RoutingTupleExtendedVersion"])
        )

    @property
    def RtmpExtendedNetworkNumber(self):
        """
        Display Name: Router's Network Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RtmpExtendedNetworkNumber"])
        )

    @property
    def RtmpExtendedNodeIDLength(self):
        """
        Display Name: Node ID length
        Default Value: 8
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RtmpExtendedNodeIDLength"])
        )

    @property
    def RtmpExtendedRouterNodeId(self):
        """
        Display Name: Router's Node ID
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RtmpExtendedRouterNodeId"])
        )

    @property
    def RoutingtupleRoutingTupleNonextendedNetworkNumber(self):
        """
        Display Name: Network Number
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RoutingtupleRoutingTupleNonextendedNetworkNumber"]
            ),
        )

    @property
    def RoutingtupleRoutingTupleNonextendedRangeFlag(self):
        """
        Display Name: Range Flag
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RoutingtupleRoutingTupleNonextendedRangeFlag"]
            ),
        )

    @property
    def RoutingtupleRoutingTupleNonextendedReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RoutingtupleRoutingTupleNonextendedReserved"]
            ),
        )

    @property
    def RoutingtupleRoutingTupleNonextendedDistance(self):
        """
        Display Name: Distance
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RoutingtupleRoutingTupleNonextendedDistance"]
            ),
        )

    @property
    def RoutingtupleRoutingTupleExtendedRangeStart(self):
        """
        Display Name: Range Start
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RoutingtupleRoutingTupleExtendedRangeStart"]
            ),
        )

    @property
    def RoutingtupleRoutingTupleExtendedRangeFlag(self):
        """
        Display Name: Range Flag
        Default Value: 1
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RoutingtupleRoutingTupleExtendedRangeFlag"]
            ),
        )

    @property
    def RoutingtupleRoutingTupleExtendedReserved(self):
        """
        Display Name: Reserved
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RoutingtupleRoutingTupleExtendedReserved"]
            ),
        )

    @property
    def RoutingtupleRoutingTupleExtendedDistance(self):
        """
        Display Name: Distance
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RoutingtupleRoutingTupleExtendedDistance"]
            ),
        )

    @property
    def RoutingtupleRoutingTupleExtendedRangeEnd(self):
        """
        Display Name: Range End
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RoutingtupleRoutingTupleExtendedRangeEnd"]
            ),
        )

    @property
    def RoutingtupleRoutingTupleExtendedVersion(self):
        """
        Display Name: Version
        Default Value: 0x82
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["RoutingtupleRoutingTupleExtendedVersion"]
            ),
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
