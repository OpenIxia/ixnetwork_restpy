# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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
    The ECpriRe class encapsulates a list of eCpriRe resources that is be managed by the user.
    A list of resources can be retrieved from the server using the ECpriRe.find() method.
    The list can be managed by the user by using the ECpriRe.add() and ECpriRe.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'eCpriRe'

    def __init__(self, parent):
        super(ECpriRe, self).__init__(parent)

    @property
    def Connector(self):
        """An instance of the Connector class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector.Connector)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.connector import Connector
        return Connector(self)

    @property
    def ECpriFaultSubObjectsList(self):
        """An instance of the ECpriFaultSubObjectsList class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprifaultsubobjectslist.ECpriFaultSubObjectsList)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ecprifaultsubobjectslist import ECpriFaultSubObjectsList
        return ECpriFaultSubObjectsList(self)

    @property
    def ActionType(self):
        """Action Type value 0x00 and 0x01 are used when an eCPRI node initiates a one-way delay measurement in direction from its own node to another node. Value 0x02 is used when an eCPRI node needs to know the one-way delay from another node to itself.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('actionType')

    @property
    def Active(self):
        """Activate/Deactivate Configuration

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('active')

    @property
    def Address(self):
        """The Address is a 48-bit value. Details such as whether the memory on the opposite node is organized in one or more memory banks or whether an address offset is signaled over the interface etc. are vendor specific. The Element ID could be used for identifying a specific memory hardware instance.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('address')

    @property
    def CompensationValue(self):
        """When Action Type is set to 0x00 (Request), 0x02 (Response) or 0x05 (Follow_Up) in the message, this field will contain the Compensation Value which is the compensation time measured in nanoseconds and multiplied by 2 to the power 16 and follows the format for the correctionField in the common message header specified in IEEE 1588-2008 Clause 13.3 [13]. When Action Type is set to 0x03 (Remote Request) or 0x04 (Remote Request with Follow_Up) the time information fields TimeStamp and Compensation Value are set to 0b in all bits. A Compensation Value of 0 (zero) is a valid value.Example: A Compensation Value of 183.5 ns is represented as 0000000000B78000 with base 16.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('compensationValue')

    @property
    def ConnectedVia(self):
        """DEPRECATED List of layers this layer used to connect to the wire

        Returns:
            list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])
        """
        return self._get_attribute('connectedVia')
    @ConnectedVia.setter
    def ConnectedVia(self, value):
        self._set_attribute('connectedVia', value)

    @property
    def Count(self):
        """Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.

        Returns:
            number
        """
        return self._get_attribute('count')

    @property
    def DelayMeasurementId(self):
        """The Measurement ID is a 1-byte value used by the sender of the request when the response is received to distinguish between different measurements, i.e. the receiver of the request shall copy the ID from the request into the response message.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('delayMeasurementId')

    @property
    def DescriptiveName(self):
        """Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context

        Returns:
            str
        """
        return self._get_attribute('descriptiveName')

    @property
    def DummyBytesLength(self):
        """The number of dummy bytes included in the eCPRI-payload will be defined by the eCPRI payload size field in the eCPRI common header. Due to network characteristics, a small message might take shorter time through the network than a large one, with the dummy bytes the one-way delay estimation can be improved. The insertion of dummy bytes is only needed when the Action Type set to 0x00 (Request) or to 0x01(Request with Follow_Up).

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('dummyBytesLength')

    @property
    def ElementId(self):
        """Depending on implementation the Element ID could be used for instance to point out a specific instance of a generic hardware function.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('elementId')

    @property
    def Errors(self):
        """A list of errors that have occurred

        Returns:
            list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))
        """
        return self._get_attribute('errors')

    @property
    def EventId(self):
        """A 1-byte value set by the transmitter of an Event Indication or a Synchronization Request to enable identification of the acknowledge response.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('eventId')

    @property
    def EventSequenceNumber(self):
        """The Sequence Number is a 1-byte value that is incremented each time the transmitter sends the Event Indication with Event Type set to 0x00 (Fault(s) Indication). The receiver will use the sequence number to ensure that the correct status for a specific combination of {Element-ID; Fault-value} is used. Due to the nature of the packet based fronthaul network, packets might be delivered out of order and a sequence number is needed to handle this scenario. When a fault indication is not acknowledged the transmitter will re-transmit the fault, setting the sequence number to the same value used in the initial transmission.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('eventSequenceNumber')

    @property
    def EventType(self):
        """Event Type value ranges from 0x00 to 0xFF, where 0x00 represents Fault(s) Indication, 0x01 represents Fault(s) Indication Acknowledge, 0x02 represents Notification(s) Indication, 0x03 represents Synchronization Request, 0x04 represents Synchronization Acknowledge, 0x05 represents Synchronization End Indication and values from 0x06 to 0xFF are Reserved.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('eventType')

    @property
    def MessageType(self):
        """Message Type

        Returns:
            str(realTimeControlData|remoteMemoryAccess|onewayDelayMeasurement|remoteReset|eventIndication)
        """
        return self._get_attribute('messageType')
    @MessageType.setter
    def MessageType(self, value):
        self._set_attribute('messageType', value)

    @property
    def Multiplier(self):
        """Number of layer instances per parent instance (multiplier)

        Returns:
            number
        """
        return self._get_attribute('multiplier')
    @Multiplier.setter
    def Multiplier(self, value):
        self._set_attribute('multiplier', value)

    @property
    def Name(self):
        """Name of NGPF element, guaranteed to be unique in Scenario

        Returns:
            str
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def NumberOfFaultSubObjects(self):
        """Number Of Fault or Notify.

        Returns:
            number
        """
        return self._get_attribute('numberOfFaultSubObjects')
    @NumberOfFaultSubObjects.setter
    def NumberOfFaultSubObjects(self, value):
        self._set_attribute('numberOfFaultSubObjects', value)

    @property
    def ReadWriteType(self):
        """The field consist of two parts, a read or write indication and a request or response indication. The Response value 0010b (Failure) is used when the receiver of the request is unable to perform the read or write request due to invalid content in received parameters or other faults.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('readWriteType')

    @property
    def RemoteResetId(self):
        """Depending on implementation the Reset ID could be used for instance to point out a specific instance of a generic hardware function. Value allocation to Reset ID is vendor specific.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('remoteResetId')

    @property
    def ReservedActionType(self):
        """The Action Type is a 1-byte value. Value 0x00 and 0x01 are used when an eCPRI node initiates a one-way delay measurement in direction from its own node to another node. Value 0x02 is used when an eCPRI node needs to know the one-way delay from another node to itself.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('reservedActionType')

    @property
    def ReservedEventType(self):
        """Reserved Event Type values from 0x06 to 0xFF are Reserved.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('reservedEventType')

    @property
    def ReservedResetCode(self):
        """The Reset Code Op is a 1-byte value. Value 0x00 represents Reserved, 0x01 represents Remote reset request, 0x02 represents Remote reset response and value ranging from 0x03 to 0xFF are Reserved.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('reservedResetCode')

    @property
    def ResetCodeOp(self):
        """The Reset Code Op is a 1-byte value. Value 0x00 represents Reserved, 0x01 represents Remote Reset Request, 0x02 represents Remote Reset Response.Values from 0x03 to 0xFF is Reserved.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('resetCodeOp')

    @property
    def RmaAction(self):
        """RMA Action Type is Request or Response or Failure.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('rmaAction')

    @property
    def RmaDataLength(self):
        """Number of bytes(0 to 255) to read or write from or to remote node.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('rmaDataLength')

    @property
    def RtcDataLength(self):
        """Size of RTC data that will be included in the eCPRI message.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('rtcDataLength')

    @property
    def SequenceId(self):
        """An identifier of each message in a series of Real-Time Control Data messages. For example, identifier of message sequence, links between request and response messages,etc. Value allocation to SEQ_ID is vendor specific.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sequenceId')

    @property
    def SessionStatus(self):
        """Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.

        Returns:
            list(str[down|notStarted|up])
        """
        return self._get_attribute('sessionStatus')

    @property
    def StackedLayers(self):
        """List of secondary (many to one) child layer protocols

        Returns:
            list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])
        """
        return self._get_attribute('stackedLayers')
    @StackedLayers.setter
    def StackedLayers(self, value):
        self._set_attribute('stackedLayers', value)

    @property
    def StartingRmaId(self):
        """Identifier of the request message used by the Initiator to match the corresponding response message.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('startingRmaId')

    @property
    def StartingRtcId(self):
        """RTC ID of the eRE or eREC.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('startingRtcId')

    @property
    def StateCounts(self):
        """A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up

        Returns:
            dict(total:number,notStarted:number,down:number,up:number)
        """
        return self._get_attribute('stateCounts')

    @property
    def Status(self):
        """Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns:
            str(configured|error|mixed|notStarted|started|starting|stopping)
        """
        return self._get_attribute('status')

    @property
    def TimeStamp(self):
        """When Action Type is set to 0x00 (Request) in the message this field will contain the time stamp t1 and when Action Type is set to 0x02 (Response) the time stamp t2. When action type is set to 0x01(Request with Follow_Up) the time stamp information fields shall be set to 0b in all bits, the corresponding time information values are sent in the Follow_Up message. When Action Type is set to 0x03 or 0x04 (Remote Request and Remote Request with Follow_Up) the time stamp information fields shall be set to 0b in all bits. When using the Follow_Up message (2-Step version) the Follow_Up message (Action Type set to 0x05) the time information values t1 and tCV1 will be set to the TimeStamp field. The time information values follow the format specified in IEEE 1588-2008 [13] Clause 5.3.3. The value consists of 2 parts, one seconds-part and one nanoseconds-part. The first 6 bytes are the seconds and the next 4 bytes are the nanoseconds.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('timeStamp')

    @property
    def VendorSpecificPayloadLength(self):
        """Vendor Specific Payload bytes are used to carry optional vendor-specific information. The vendor specific information can contain data items such as authentication parameters or any parameters to select a specific reset behavior. This specification does not detail any concrete reset behavior.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('vendorSpecificPayloadLength')

    def update(self, ConnectedVia=None, MessageType=None, Multiplier=None, Name=None, NumberOfFaultSubObjects=None, StackedLayers=None):
        """Updates a child instance of eCpriRe on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args:
            ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
            MessageType (str(realTimeControlData|remoteMemoryAccess|onewayDelayMeasurement|remoteReset|eventIndication)): Message Type
            Multiplier (number): Number of layer instances per parent instance (multiplier)
            Name (str): Name of NGPF element, guaranteed to be unique in Scenario
            NumberOfFaultSubObjects (number): Number Of Fault or Notify.
            StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, ConnectedVia=None, MessageType=None, Multiplier=None, Name=None, NumberOfFaultSubObjects=None, StackedLayers=None):
        """Adds a new eCpriRe node on the server and retrieves it in this instance.

        Args:
            ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
            MessageType (str(realTimeControlData|remoteMemoryAccess|onewayDelayMeasurement|remoteReset|eventIndication)): Message Type
            Multiplier (number): Number of layer instances per parent instance (multiplier)
            Name (str): Name of NGPF element, guaranteed to be unique in Scenario
            NumberOfFaultSubObjects (number): Number Of Fault or Notify.
            StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols

        Returns:
            self: This instance with all currently retrieved eCpriRe data using find and the newly added eCpriRe data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the eCpriRe data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectedVia=None, Count=None, DescriptiveName=None, Errors=None, MessageType=None, Multiplier=None, Name=None, NumberOfFaultSubObjects=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None):
        """Finds and retrieves eCpriRe data from the server.

        All named parameters support regex and can be used to selectively retrieve eCpriRe data from the server.
        By default the find method takes no parameters and will retrieve all eCpriRe data from the server.

        Args:
            ConnectedVia (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of layers this layer used to connect to the wire
            Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
            DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
            Errors (list(dict(arg1:str[None|/api/v1/sessions/1/ixnetwork/?deepchild=*],arg2:list[str]))): A list of errors that have occurred
            MessageType (str(realTimeControlData|remoteMemoryAccess|onewayDelayMeasurement|remoteReset|eventIndication)): Message Type
            Multiplier (number): Number of layer instances per parent instance (multiplier)
            Name (str): Name of NGPF element, guaranteed to be unique in Scenario
            NumberOfFaultSubObjects (number): Number Of Fault or Notify.
            SessionStatus (list(str[down|notStarted|up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
            StackedLayers (list(str[None|/api/v1/sessions/1/ixnetwork/topology?deepchild=*])): List of secondary (many to one) child layer protocols
            StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
            Status (str(configured|error|mixed|notStarted|started|starting|stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns:
            self: This instance with matching eCpriRe data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of eCpriRe data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the eCpriRe data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, ActionType=None, Active=None, Address=None, CompensationValue=None, DelayMeasurementId=None, DummyBytesLength=None, ElementId=None, EventId=None, EventSequenceNumber=None, EventType=None, ReadWriteType=None, RemoteResetId=None, ReservedActionType=None, ReservedEventType=None, ReservedResetCode=None, ResetCodeOp=None, RmaAction=None, RmaDataLength=None, RtcDataLength=None, SequenceId=None, StartingRmaId=None, StartingRtcId=None, TimeStamp=None, VendorSpecificPayloadLength=None):
        """Base class infrastructure that gets a list of eCpriRe device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args:
            PortNames (str): optional regex of port names
            ActionType (str): optional regex of actionType
            Active (str): optional regex of active
            Address (str): optional regex of address
            CompensationValue (str): optional regex of compensationValue
            DelayMeasurementId (str): optional regex of delayMeasurementId
            DummyBytesLength (str): optional regex of dummyBytesLength
            ElementId (str): optional regex of elementId
            EventId (str): optional regex of eventId
            EventSequenceNumber (str): optional regex of eventSequenceNumber
            EventType (str): optional regex of eventType
            ReadWriteType (str): optional regex of readWriteType
            RemoteResetId (str): optional regex of remoteResetId
            ReservedActionType (str): optional regex of reservedActionType
            ReservedEventType (str): optional regex of reservedEventType
            ReservedResetCode (str): optional regex of reservedResetCode
            ResetCodeOp (str): optional regex of resetCodeOp
            RmaAction (str): optional regex of rmaAction
            RmaDataLength (str): optional regex of rmaDataLength
            RtcDataLength (str): optional regex of rtcDataLength
            SequenceId (str): optional regex of sequenceId
            StartingRmaId (str): optional regex of startingRmaId
            StartingRtcId (str): optional regex of startingRtcId
            TimeStamp (str): optional regex of timeStamp
            VendorSpecificPayloadLength (str): optional regex of vendorSpecificPayloadLength

        Returns:
            list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def RestartDown(self, *args, **kwargs):
        """Executes the restartDown operation on the server.

        Stop and start interfaces and sessions that are in Down state.

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        restartDown()

        restartDown(SessionIndices:list)
            Args:
                args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        restartDown(SessionIndices:string)
            Args:
                args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('restartDown', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        Start selected protocols.

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        start()

        start(SessionIndices:list)
            Args:
                args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        start(SessionIndices:string)
            Args:
                args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        """Executes the stop operation on the server.

        Stop selected protocols.

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        stop()

        stop(SessionIndices:list)
            Args:
                args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        stop(SessionIndices:string)
            Args:
                args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)
