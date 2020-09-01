# MIT LICENSE
#
# Copyright 1997 - 2020 by IXIA Keysight
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE. 
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files


class ECpriRe(Base):
    """EcpriRe
    The ECpriRe class encapsulates a list of eCpriRe resources that are managed by the user.
    A list of resources can be retrieved from the server using the ECpriRe.find() method.
    The list can be managed by using the ECpriRe.add() and ECpriRe.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'eCpriRe'
    _SDM_ATT_MAP = {
        'ActionType': 'actionType',
        'Active': 'active',
        'Address': 'address',
        'CompensationValue': 'compensationValue',
        'ConnectedVia': 'connectedVia',
        'Count': 'count',
        'DelayMeasurementId': 'delayMeasurementId',
        'DescriptiveName': 'descriptiveName',
        'DummyBytesLength': 'dummyBytesLength',
        'ElementId': 'elementId',
        'Errors': 'errors',
        'EventId': 'eventId',
        'EventSequenceNumber': 'eventSequenceNumber',
        'EventType': 'eventType',
        'MessageType': 'messageType',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'NumberOfFaultSubObjects': 'numberOfFaultSubObjects',
        'ReadWriteType': 'readWriteType',
        'RemoteResetId': 'remoteResetId',
        'ReservedActionType': 'reservedActionType',
        'ReservedEventType': 'reservedEventType',
        'ReservedResetCode': 'reservedResetCode',
        'ResetCodeOp': 'resetCodeOp',
        'RmaAction': 'rmaAction',
        'RmaDataLength': 'rmaDataLength',
        'RtcDataLength': 'rtcDataLength',
        'SequenceId': 'sequenceId',
        'SessionStatus': 'sessionStatus',
        'StackedLayers': 'stackedLayers',
        'StartingRmaId': 'startingRmaId',
        'StartingRtcId': 'startingRtcId',
        'StateCounts': 'stateCounts',
        'Status': 'status',
        'TimeStamp': 'timeStamp',
        'VendorSpecificPayloadLength': 'vendorSpecificPayloadLength',
    }

    def __init__(self, parent):
        super(ECpriRe, self).__init__(parent)

    @property
    def Connector(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector_d0d942810e4010add7642d3914a1f29b.Connector): An instance of the Connector class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector_d0d942810e4010add7642d3914a1f29b import Connector
        return Connector(self)

    @property
    def ECpriFaultSubObjectsList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprifaultsubobjectslist_066a935ffc4b8b88998000da08d713eb.ECpriFaultSubObjectsList): An instance of the ECpriFaultSubObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprifaultsubobjectslist_066a935ffc4b8b88998000da08d713eb import ECpriFaultSubObjectsList
        return ECpriFaultSubObjectsList(self)

    @property
    def ActionType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Action Type value 0x00 and 0x01 are used when an eCPRI node initiates a one-way delay measurement in direction from its own node to another node. Value 0x02 is used when an eCPRI node needs to know the one-way delay from another node to itself.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ActionType']))

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def Address(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Address is a 48-bit value. Details such as whether the memory on the opposite node is organized in one or more memory banks or whether an address offset is signaled over the interface etc. are vendor specific. The Element ID could be used for identifying a specific memory hardware instance.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Address']))

    @property
    def CompensationValue(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): When Action Type is set to 0x00 (Request), 0x02 (Response) or 0x05 (Follow_Up) in the message, this field will contain the Compensation Value which is the compensation time measured in nanoseconds and multiplied by 2 to the power 16 and follows the format for the correctionField in the common message header specified in IEEE 1588-2008 Clause 13.3 [13]. When Action Type is set to 0x03 (Remote Request) or 0x04 (Remote Request with Follow_Up) the time information fields TimeStamp and Compensation Value are set to 0b in all bits. A Compensation Value of 0 (zero) is a valid value.Example: A Compensation Value of 183.5 ns is represented as 0000000000B78000 with base 16.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['CompensationValue']))

    @property
    def ConnectedVia(self):
        """DEPRECATED 
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of layers this layer is used to connect with to the wire.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConnectedVia'])
    @ConnectedVia.setter
    def ConnectedVia(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ConnectedVia'], value)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DelayMeasurementId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Measurement ID is a 1-byte value used by the sender of the request when the response is received to distinguish between different measurements, i.e. the receiver of the request shall copy the ID from the request into the response message.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DelayMeasurementId']))

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def DummyBytesLength(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The number of dummy bytes included in the eCPRI-payload will be defined by the eCPRI payload size field in the eCPRI common header. Due to network characteristics, a small message might take shorter time through the network than a large one, with the dummy bytes the one-way delay estimation can be improved. The insertion of dummy bytes is only needed when the Action Type set to 0x00 (Request) or to 0x01(Request with Follow_Up).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DummyBytesLength']))

    @property
    def ElementId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Depending on implementation the Element ID could be used for instance to point out a specific instance of a generic hardware function.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ElementId']))

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

    @property
    def EventId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A 1-byte value set by the transmitter of an Event Indication or a Synchronization Request to enable identification of the acknowledge response.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EventId']))

    @property
    def EventSequenceNumber(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Sequence Number is a 1-byte value that is incremented each time the transmitter sends the Event Indication with Event Type set to 0x00 (Fault(s) Indication). The receiver will use the sequence number to ensure that the correct status for a specific combination of {Element-ID; Fault-value} is used. Due to the nature of the packet based fronthaul network, packets might be delivered out of order and a sequence number is needed to handle this scenario. When a fault indication is not acknowledged the transmitter will re-transmit the fault, setting the sequence number to the same value used in the initial transmission.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EventSequenceNumber']))

    @property
    def EventType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Event Type value ranges from 0x00 to 0xFF, where 0x00 represents Fault(s) Indication, 0x01 represents Fault(s) Indication Acknowledge, 0x02 represents Notification(s) Indication, 0x03 represents Synchronization Request, 0x04 represents Synchronization Acknowledge, 0x05 represents Synchronization End Indication and values from 0x06 to 0xFF are Reserved.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EventType']))

    @property
    def MessageType(self):
        """
        Returns
        -------
        - str(realTimeControlData | remoteMemoryAccess | onewayDelayMeasurement | remoteReset | eventIndication): Message Type
        """
        return self._get_attribute(self._SDM_ATT_MAP['MessageType'])
    @MessageType.setter
    def MessageType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MessageType'], value)

    @property
    def Multiplier(self):
        """
        Returns
        -------
        - number: Number of layer instances per parent instance (multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Multiplier'])
    @Multiplier.setter
    def Multiplier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Multiplier'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def NumberOfFaultSubObjects(self):
        """
        Returns
        -------
        - number: Number Of Fault or Notify.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfFaultSubObjects'])
    @NumberOfFaultSubObjects.setter
    def NumberOfFaultSubObjects(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfFaultSubObjects'], value)

    @property
    def ReadWriteType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The field consist of two parts, a read or write indication and a request or response indication. The Response value 0010b (Failure) is used when the receiver of the request is unable to perform the read or write request due to invalid content in received parameters or other faults.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReadWriteType']))

    @property
    def RemoteResetId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Depending on implementation the Reset ID could be used for instance to point out a specific instance of a generic hardware function. Value allocation to Reset ID is vendor specific.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RemoteResetId']))

    @property
    def ReservedActionType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Action Type is a 1-byte value. Value 0x00 and 0x01 are used when an eCPRI node initiates a one-way delay measurement in direction from its own node to another node. Value 0x02 is used when an eCPRI node needs to know the one-way delay from another node to itself.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReservedActionType']))

    @property
    def ReservedEventType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Reserved Event Type values from 0x06 to 0xFF are Reserved.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReservedEventType']))

    @property
    def ReservedResetCode(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Reset Code Op is a 1-byte value. Value 0x00 represents Reserved, 0x01 represents Remote reset request, 0x02 represents Remote reset response and value ranging from 0x03 to 0xFF are Reserved.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ReservedResetCode']))

    @property
    def ResetCodeOp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Reset Code Op is a 1-byte value. Value 0x00 represents Reserved, 0x01 represents Remote Reset Request, 0x02 represents Remote Reset Response.Values from 0x03 to 0xFF is Reserved.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ResetCodeOp']))

    @property
    def RmaAction(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RMA Action Type is Request or Response or Failure.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RmaAction']))

    @property
    def RmaDataLength(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of bytes(0 to 255) to read or write from or to remote node.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RmaDataLength']))

    @property
    def RtcDataLength(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Size of RTC data that will be included in the eCPRI message.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['RtcDataLength']))

    @property
    def SequenceId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): An identifier of each message in a series of Real-Time Control Data messages. For example, identifier of message sequence, links between request and response messages,etc. Value allocation to SEQ_ID is vendor specific.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SequenceId']))

    @property
    def SessionStatus(self):
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SessionStatus'])

    @property
    def StackedLayers(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of secondary (many to one) child layer protocols
        """
        return self._get_attribute(self._SDM_ATT_MAP['StackedLayers'])
    @StackedLayers.setter
    def StackedLayers(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StackedLayers'], value)

    @property
    def StartingRmaId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Identifier of the request message used by the Initiator to match the corresponding response message.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartingRmaId']))

    @property
    def StartingRtcId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RTC ID of the eRE or eREC.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['StartingRtcId']))

    @property
    def StateCounts(self):
        """
        Returns
        -------
        - dict(total:number,notStarted:number,down:number,up:number): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        """
        return self._get_attribute(self._SDM_ATT_MAP['StateCounts'])

    @property
    def Status(self):
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Status'])

    @property
    def TimeStamp(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): When Action Type is set to 0x00 (Request) in the message this field will contain the time stamp t1 and when Action Type is set to 0x02 (Response) the time stamp t2. When action type is set to 0x01(Request with Follow_Up) the time stamp information fields shall be set to 0b in all bits, the corresponding time information values are sent in the Follow_Up message. When Action Type is set to 0x03 or 0x04 (Remote Request and Remote Request with Follow_Up) the time stamp information fields shall be set to 0b in all bits. When using the Follow_Up message (2-Step version) the Follow_Up message (Action Type set to 0x05) the time information values t1 and tCV1 will be set to the TimeStamp field. The time information values follow the format specified in IEEE 1588-2008 [13] Clause 5.3.3. The value consists of 2 parts, one seconds-part and one nanoseconds-part. The first 6 bytes are the seconds and the next 4 bytes are the nanoseconds.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TimeStamp']))

    @property
    def VendorSpecificPayloadLength(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Vendor Specific Payload bytes are used to carry optional vendor-specific information. The vendor specific information can contain data items such as authentication parameters or any parameters to select a specific reset behavior. This specification does not detail any concrete reset behavior.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VendorSpecificPayloadLength']))

    def update(self, ConnectedVia=None, MessageType=None, Multiplier=None, Name=None, NumberOfFaultSubObjects=None, StackedLayers=None):
        """Updates eCpriRe resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - MessageType (str(realTimeControlData | remoteMemoryAccess | onewayDelayMeasurement | remoteReset | eventIndication)): Message Type
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfFaultSubObjects (number): Number Of Fault or Notify.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, ConnectedVia=None, MessageType=None, Multiplier=None, Name=None, NumberOfFaultSubObjects=None, StackedLayers=None):
        """Adds a new eCpriRe resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - MessageType (str(realTimeControlData | remoteMemoryAccess | onewayDelayMeasurement | remoteReset | eventIndication)): Message Type
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfFaultSubObjects (number): Number Of Fault or Notify.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved eCpriRe resources using find and the newly added eCpriRe resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained eCpriRe resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectedVia=None, Count=None, DescriptiveName=None, Errors=None, MessageType=None, Multiplier=None, Name=None, NumberOfFaultSubObjects=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None):
        """Finds and retrieves eCpriRe resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve eCpriRe resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all eCpriRe resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - MessageType (str(realTimeControlData | remoteMemoryAccess | onewayDelayMeasurement | remoteReset | eventIndication)): Message Type
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfFaultSubObjects (number): Number Of Fault or Notify.
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching eCpriRe resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of eCpriRe data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the eCpriRe resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, ActionType=None, Active=None, Address=None, CompensationValue=None, DelayMeasurementId=None, DummyBytesLength=None, ElementId=None, EventId=None, EventSequenceNumber=None, EventType=None, ReadWriteType=None, RemoteResetId=None, ReservedActionType=None, ReservedEventType=None, ReservedResetCode=None, ResetCodeOp=None, RmaAction=None, RmaDataLength=None, RtcDataLength=None, SequenceId=None, StartingRmaId=None, StartingRtcId=None, TimeStamp=None, VendorSpecificPayloadLength=None):
        """Base class infrastructure that gets a list of eCpriRe device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - ActionType (str): optional regex of actionType
        - Active (str): optional regex of active
        - Address (str): optional regex of address
        - CompensationValue (str): optional regex of compensationValue
        - DelayMeasurementId (str): optional regex of delayMeasurementId
        - DummyBytesLength (str): optional regex of dummyBytesLength
        - ElementId (str): optional regex of elementId
        - EventId (str): optional regex of eventId
        - EventSequenceNumber (str): optional regex of eventSequenceNumber
        - EventType (str): optional regex of eventType
        - ReadWriteType (str): optional regex of readWriteType
        - RemoteResetId (str): optional regex of remoteResetId
        - ReservedActionType (str): optional regex of reservedActionType
        - ReservedEventType (str): optional regex of reservedEventType
        - ReservedResetCode (str): optional regex of reservedResetCode
        - ResetCodeOp (str): optional regex of resetCodeOp
        - RmaAction (str): optional regex of rmaAction
        - RmaDataLength (str): optional regex of rmaDataLength
        - RtcDataLength (str): optional regex of rtcDataLength
        - SequenceId (str): optional regex of sequenceId
        - StartingRmaId (str): optional regex of startingRmaId
        - StartingRtcId (str): optional regex of startingRtcId
        - TimeStamp (str): optional regex of timeStamp
        - VendorSpecificPayloadLength (str): optional regex of vendorSpecificPayloadLength

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def Abort(self, *args, **kwargs):
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        abort(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        abort(SessionIndices=string)
        ----------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('abort', payload=payload, response_object=None)

    def RestartDown(self, *args, **kwargs):
        """Executes the restartDown operation on the server.

        Stop and start interfaces and sessions that are in Down state.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        restartDown(SessionIndices=list)
        --------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        restartDown(SessionIndices=string)
        ----------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('restartDown', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        start(SessionIndices=string)
        ----------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(SessionIndices=list)
        -------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        stop(SessionIndices=string)
        ---------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)
