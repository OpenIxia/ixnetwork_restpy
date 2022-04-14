from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class MsrpVectorAttribute(Base):
    __slots__ = ()
    _SDM_NAME = "msrpVectorAttribute"
    _SDM_ATT_MAP = {
        "VectorHeaderLeaveAllEvent": "msrpVectorAttribute.header.vectorHeader.leaveAllEvent-1",
        "VectorHeaderNoOfValues": "msrpVectorAttribute.header.vectorHeader.noOfValues-2",
        "StreamIdSourceAddress": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerAdvertiseFirstValue.streamId.sourceAddress-3",
        "StreamIdUniqueId": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerAdvertiseFirstValue.streamId.uniqueId-4",
        "DataFrameParametersDestinationAddress": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerAdvertiseFirstValue.dataFrameParameters.destinationAddress-5",
        "DataFrameParametersVlanIdentifier": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerAdvertiseFirstValue.dataFrameParameters.vlanIdentifier-6",
        "TSpecMaxFrameSize": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerAdvertiseFirstValue.tSpec.maxFrameSize-7",
        "TSpecMaxIntervalFrames": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerAdvertiseFirstValue.tSpec.maxIntervalFrames-8",
        "TSpecDataFramePriority": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerAdvertiseFirstValue.tSpec.dataFramePriority-9",
        "TSpecRank": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerAdvertiseFirstValue.tSpec.rank-10",
        "TSpecReserved": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerAdvertiseFirstValue.tSpec.reserved-11",
        "MsrptalkeradvertisefirstvalueTSpecMaxFrameSize": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerAdvertiseFirstValue.tSpec.maxFrameSize-12",
        "MsrptalkeradvertisefirstvalueTSpecMaxIntervalFrames": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerAdvertiseFirstValue.tSpec.maxIntervalFrames-13",
        "MsrptalkeradvertisefirstvalueTSpecDataFramePriority": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerAdvertiseFirstValue.tSpec.dataFramePriority-14",
        "MsrptalkeradvertisefirstvalueTSpecRank": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerAdvertiseFirstValue.tSpec.rank-15",
        "MsrptalkeradvertisefirstvalueTSpecReserved": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerAdvertiseFirstValue.tSpec.reserved-16",
        "MsrpTalkerAdvertiseFirstValueAccumulatedLatency": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerAdvertiseFirstValue.accumulatedLatency-17",
        "MsrptalkerfailedfirstvalueStreamIdSourceAddress": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerFailedFirstValue.streamId.sourceAddress-18",
        "MsrptalkerfailedfirstvalueStreamIdUniqueId": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerFailedFirstValue.streamId.uniqueId-19",
        "MsrptalkerfailedfirstvalueDataFrameParametersDestinationAddress": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerFailedFirstValue.dataFrameParameters.destinationAddress-20",
        "MsrptalkerfailedfirstvalueDataFrameParametersVlanIdentifier": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerFailedFirstValue.dataFrameParameters.vlanIdentifier-21",
        "MsrptalkerfailedfirstvalueTSpecMaxFrameSize": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerFailedFirstValue.tSpec.maxFrameSize-22",
        "MsrptalkerfailedfirstvalueTSpecMaxIntervalFrames": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerFailedFirstValue.tSpec.maxIntervalFrames-23",
        "MsrptalkerfailedfirstvalueTSpecDataFramePriority": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerFailedFirstValue.tSpec.dataFramePriority-24",
        "MsrptalkerfailedfirstvalueTSpecRank": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerFailedFirstValue.tSpec.rank-25",
        "MsrptalkerfailedfirstvalueTSpecReserved": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerFailedFirstValue.tSpec.reserved-26",
        "TSpecBridgeId": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerFailedFirstValue.tSpec.bridgeId-27",
        "TSpecFailureCode": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerFailedFirstValue.tSpec.failureCode-28",
        "MsrptalkerfailedfirstvalueTSpecMaxFrameSize": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerFailedFirstValue.tSpec.maxFrameSize-29",
        "MsrptalkerfailedfirstvalueTSpecMaxIntervalFrames": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerFailedFirstValue.tSpec.maxIntervalFrames-30",
        "MsrptalkerfailedfirstvalueTSpecDataFramePriority": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerFailedFirstValue.tSpec.dataFramePriority-31",
        "MsrptalkerfailedfirstvalueTSpecRank": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerFailedFirstValue.tSpec.rank-32",
        "MsrptalkerfailedfirstvalueTSpecReserved": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerFailedFirstValue.tSpec.reserved-33",
        "MsrptalkerfailedfirstvalueTSpecBridgeId": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerFailedFirstValue.tSpec.bridgeId-34",
        "MsrptalkerfailedfirstvalueTSpecFailureCode": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerFailedFirstValue.tSpec.failureCode-35",
        "MsrpTalkerFailedFirstValueAccumulatedLatency": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerFailedFirstValue.accumulatedLatency-36",
        "MsrptalkerfailedfirstvalueTSpecMaxFrameSize": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerFailedFirstValue.tSpec.maxFrameSize-37",
        "MsrptalkerfailedfirstvalueTSpecMaxIntervalFrames": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerFailedFirstValue.tSpec.maxIntervalFrames-38",
        "MsrptalkerfailedfirstvalueTSpecDataFramePriority": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerFailedFirstValue.tSpec.dataFramePriority-39",
        "MsrptalkerfailedfirstvalueTSpecRank": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerFailedFirstValue.tSpec.rank-40",
        "MsrptalkerfailedfirstvalueTSpecReserved": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerFailedFirstValue.tSpec.reserved-41",
        "MsrptalkerfailedfirstvalueTSpecBridgeId": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerFailedFirstValue.tSpec.bridgeId-42",
        "MsrptalkerfailedfirstvalueTSpecFailureCode": "msrpVectorAttribute.header.selectFirstValueType.msrpTalkerFailedFirstValue.tSpec.failureCode-43",
        "MsrplistenervectorStreamIdSourceAddress": "msrpVectorAttribute.header.selectFirstValueType.msrpListenerVector.streamId.sourceAddress-44",
        "MsrplistenervectorStreamIdUniqueId": "msrpVectorAttribute.header.selectFirstValueType.msrpListenerVector.streamId.uniqueId-45",
        "MsrpDomainVectorSrClassID": "msrpVectorAttribute.header.selectFirstValueType.msrpDomainVector.srClassID-46",
        "MsrpDomainVectorSrClassPriority": "msrpVectorAttribute.header.selectFirstValueType.msrpDomainVector.srClassPriority-47",
        "MsrpDomainVectorSrClassVid": "msrpVectorAttribute.header.selectFirstValueType.msrpDomainVector.srClassVid-48",
    }

    def __init__(self, parent, list_op=False):
        super(MsrpVectorAttribute, self).__init__(parent, list_op)

    @property
    def VectorHeaderLeaveAllEvent(self):
        """
        Display Name: Leave All Event
        Default Value: 0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VectorHeaderLeaveAllEvent"])
        )

    @property
    def VectorHeaderNoOfValues(self):
        """
        Display Name: No Of Values
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VectorHeaderNoOfValues"])
        )

    @property
    def StreamIdSourceAddress(self):
        """
        Display Name: Source Address
        Default Value: 0x222222222222
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["StreamIdSourceAddress"])
        )

    @property
    def StreamIdUniqueId(self):
        """
        Display Name: Unique ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["StreamIdUniqueId"])
        )

    @property
    def DataFrameParametersDestinationAddress(self):
        """
        Display Name: Destination Address
        Default Value: 0x91E0F000FE00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["DataFrameParametersDestinationAddress"]
            ),
        )

    @property
    def DataFrameParametersVlanIdentifier(self):
        """
        Display Name: VLAN Identifier
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["DataFrameParametersVlanIdentifier"]),
        )

    @property
    def TSpecMaxFrameSize(self):
        """
        Display Name: Max Frame Size
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TSpecMaxFrameSize"])
        )

    @property
    def TSpecMaxIntervalFrames(self):
        """
        Display Name: Max Interval Frames
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TSpecMaxIntervalFrames"])
        )

    @property
    def TSpecDataFramePriority(self):
        """
        Display Name: Data Frame Priority
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TSpecDataFramePriority"])
        )

    @property
    def TSpecRank(self):
        """
        Display Name: Rank
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TSpecRank"]))

    @property
    def TSpecReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TSpecReserved"]))

    @property
    def MsrptalkeradvertisefirstvalueTSpecMaxFrameSize(self):
        """
        Display Name: Max Frame Size
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrptalkeradvertisefirstvalueTSpecMaxFrameSize"]
            ),
        )

    @property
    def MsrptalkeradvertisefirstvalueTSpecMaxIntervalFrames(self):
        """
        Display Name: Max Interval Frames
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrptalkeradvertisefirstvalueTSpecMaxIntervalFrames"]
            ),
        )

    @property
    def MsrptalkeradvertisefirstvalueTSpecDataFramePriority(self):
        """
        Display Name: Data Frame Priority
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrptalkeradvertisefirstvalueTSpecDataFramePriority"]
            ),
        )

    @property
    def MsrptalkeradvertisefirstvalueTSpecRank(self):
        """
        Display Name: Rank
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrptalkeradvertisefirstvalueTSpecRank"]
            ),
        )

    @property
    def MsrptalkeradvertisefirstvalueTSpecReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrptalkeradvertisefirstvalueTSpecReserved"]
            ),
        )

    @property
    def MsrpTalkerAdvertiseFirstValueAccumulatedLatency(self):
        """
        Display Name: Accumulated Latency
        Default Value: 20
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrpTalkerAdvertiseFirstValueAccumulatedLatency"]
            ),
        )

    @property
    def MsrptalkerfailedfirstvalueStreamIdSourceAddress(self):
        """
        Display Name: Source Address
        Default Value: 0x222222222222
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrptalkerfailedfirstvalueStreamIdSourceAddress"]
            ),
        )

    @property
    def MsrptalkerfailedfirstvalueStreamIdUniqueId(self):
        """
        Display Name: Unique ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrptalkerfailedfirstvalueStreamIdUniqueId"]
            ),
        )

    @property
    def MsrptalkerfailedfirstvalueDataFrameParametersDestinationAddress(self):
        """
        Display Name: Destination Address
        Default Value: 0x91E0F000FE00
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MsrptalkerfailedfirstvalueDataFrameParametersDestinationAddress"
                ]
            ),
        )

    @property
    def MsrptalkerfailedfirstvalueDataFrameParametersVlanIdentifier(self):
        """
        Display Name: VLAN Identifier
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP[
                    "MsrptalkerfailedfirstvalueDataFrameParametersVlanIdentifier"
                ]
            ),
        )

    @property
    def MsrptalkerfailedfirstvalueTSpecMaxFrameSize(self):
        """
        Display Name: Max Frame Size
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrptalkerfailedfirstvalueTSpecMaxFrameSize"]
            ),
        )

    @property
    def MsrptalkerfailedfirstvalueTSpecMaxIntervalFrames(self):
        """
        Display Name: Max Interval Frames
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrptalkerfailedfirstvalueTSpecMaxIntervalFrames"]
            ),
        )

    @property
    def MsrptalkerfailedfirstvalueTSpecDataFramePriority(self):
        """
        Display Name: Data Frame Priority
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrptalkerfailedfirstvalueTSpecDataFramePriority"]
            ),
        )

    @property
    def MsrptalkerfailedfirstvalueTSpecRank(self):
        """
        Display Name: Rank
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrptalkerfailedfirstvalueTSpecRank"]
            ),
        )

    @property
    def MsrptalkerfailedfirstvalueTSpecReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrptalkerfailedfirstvalueTSpecReserved"]
            ),
        )

    @property
    def TSpecBridgeId(self):
        """
        Display Name: Bridge ID
        Default Value: 0x22222222228000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TSpecBridgeId"]))

    @property
    def TSpecFailureCode(self):
        """
        Display Name: Failure Code
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["TSpecFailureCode"])
        )

    @property
    def MsrptalkerfailedfirstvalueTSpecMaxFrameSize(self):
        """
        Display Name: Max Frame Size
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrptalkerfailedfirstvalueTSpecMaxFrameSize"]
            ),
        )

    @property
    def MsrptalkerfailedfirstvalueTSpecMaxIntervalFrames(self):
        """
        Display Name: Max Interval Frames
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrptalkerfailedfirstvalueTSpecMaxIntervalFrames"]
            ),
        )

    @property
    def MsrptalkerfailedfirstvalueTSpecDataFramePriority(self):
        """
        Display Name: Data Frame Priority
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrptalkerfailedfirstvalueTSpecDataFramePriority"]
            ),
        )

    @property
    def MsrptalkerfailedfirstvalueTSpecRank(self):
        """
        Display Name: Rank
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrptalkerfailedfirstvalueTSpecRank"]
            ),
        )

    @property
    def MsrptalkerfailedfirstvalueTSpecReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrptalkerfailedfirstvalueTSpecReserved"]
            ),
        )

    @property
    def MsrptalkerfailedfirstvalueTSpecBridgeId(self):
        """
        Display Name: Bridge ID
        Default Value: 0x22222222228000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrptalkerfailedfirstvalueTSpecBridgeId"]
            ),
        )

    @property
    def MsrptalkerfailedfirstvalueTSpecFailureCode(self):
        """
        Display Name: Failure Code
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrptalkerfailedfirstvalueTSpecFailureCode"]
            ),
        )

    @property
    def MsrpTalkerFailedFirstValueAccumulatedLatency(self):
        """
        Display Name: Accumulated Latency
        Default Value: 20
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrpTalkerFailedFirstValueAccumulatedLatency"]
            ),
        )

    @property
    def MsrptalkerfailedfirstvalueTSpecMaxFrameSize(self):
        """
        Display Name: Max Frame Size
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrptalkerfailedfirstvalueTSpecMaxFrameSize"]
            ),
        )

    @property
    def MsrptalkerfailedfirstvalueTSpecMaxIntervalFrames(self):
        """
        Display Name: Max Interval Frames
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrptalkerfailedfirstvalueTSpecMaxIntervalFrames"]
            ),
        )

    @property
    def MsrptalkerfailedfirstvalueTSpecDataFramePriority(self):
        """
        Display Name: Data Frame Priority
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrptalkerfailedfirstvalueTSpecDataFramePriority"]
            ),
        )

    @property
    def MsrptalkerfailedfirstvalueTSpecRank(self):
        """
        Display Name: Rank
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrptalkerfailedfirstvalueTSpecRank"]
            ),
        )

    @property
    def MsrptalkerfailedfirstvalueTSpecReserved(self):
        """
        Display Name: Reserved
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrptalkerfailedfirstvalueTSpecReserved"]
            ),
        )

    @property
    def MsrptalkerfailedfirstvalueTSpecBridgeId(self):
        """
        Display Name: Bridge ID
        Default Value: 0x22222222228000
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrptalkerfailedfirstvalueTSpecBridgeId"]
            ),
        )

    @property
    def MsrptalkerfailedfirstvalueTSpecFailureCode(self):
        """
        Display Name: Failure Code
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrptalkerfailedfirstvalueTSpecFailureCode"]
            ),
        )

    @property
    def MsrplistenervectorStreamIdSourceAddress(self):
        """
        Display Name: Source Address
        Default Value: 0x222222222222
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrplistenervectorStreamIdSourceAddress"]
            ),
        )

    @property
    def MsrplistenervectorStreamIdUniqueId(self):
        """
        Display Name: Unique ID
        Default Value: 0x0
        Value Format: hex
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(
                self._SDM_ATT_MAP["MsrplistenervectorStreamIdUniqueId"]
            ),
        )

    @property
    def MsrpDomainVectorSrClassID(self):
        """
        Display Name: SR Class ID
        Default Value: 6
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MsrpDomainVectorSrClassID"])
        )

    @property
    def MsrpDomainVectorSrClassPriority(self):
        """
        Display Name: SR Class Priority
        Default Value: 0
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["MsrpDomainVectorSrClassPriority"]),
        )

    @property
    def MsrpDomainVectorSrClassVid(self):
        """
        Display Name: SR Class VID
        Default Value: 2
        Value Format: decimal
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["MsrpDomainVectorSrClassVid"])
        )

    def add(self):
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))
