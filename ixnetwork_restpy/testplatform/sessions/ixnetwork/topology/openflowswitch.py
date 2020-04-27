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


class OpenFlowSwitch(Base):
    """OpenFlow Session (Device) level Configuration
    The OpenFlowSwitch class encapsulates a list of openFlowSwitch resources that are managed by the user.
    A list of resources can be retrieved from the server using the OpenFlowSwitch.find() method.
    The list can be managed by using the OpenFlowSwitch.add() and OpenFlowSwitch.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'openFlowSwitch'

    def __init__(self, parent):
        super(OpenFlowSwitch, self).__init__(parent)

    @property
    def OFSwitchChannel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ofswitchchannel.OFSwitchChannel): An instance of the OFSwitchChannel class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ofswitchchannel import OFSwitchChannel
        return OFSwitchChannel(self)

    @property
    def LearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo.LearnedInfo): An instance of the LearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo import LearnedInfo
        return LearnedInfo(self)

    @property
    def OFSwitchLearnedInfoConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ofswitchlearnedinfoconfig.OFSwitchLearnedInfoConfig): An instance of the OFSwitchLearnedInfoConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ofswitchlearnedinfoconfig import OFSwitchLearnedInfoConfig
        return OFSwitchLearnedInfoConfig(self)._select()

    @property
    def OfSwitchPorts(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ofswitchports.OfSwitchPorts): An instance of the OfSwitchPorts class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ofswitchports import OfSwitchPorts
        return OfSwitchPorts(self)._select()

    @property
    def PacketInList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.packetinlist.PacketInList): An instance of the PacketInList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.packetinlist import PacketInList
        return PacketInList(self)

    @property
    def SwitchGroupsList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.switchgroupslist.SwitchGroupsList): An instance of the SwitchGroupsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.switchgroupslist import SwitchGroupsList
        return SwitchGroupsList(self)

    @property
    def SwitchTablesList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.switchtableslist.SwitchTablesList): An instance of the SwitchTablesList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.switchtableslist import SwitchTablesList
        return SwitchTablesList(self)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('active'))

    @property
    def AuxConnTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The inactive time in milliseconds after which the auxiliary connection will timeout and close.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('auxConnTimeout'))

    @property
    def AuxNonHelloStartupOption(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify the action from the following options for non-hello message when connection is established. The options are: 1) Accept Connection 2) Return Error
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('auxNonHelloStartupOption'))

    @property
    def BadVersionErrorAction(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify the action to be performed when an invalid version error occurs. The options are: 1) Re-send Hello 2) Terminate Connection
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('badVersionErrorAction'))

    @property
    def BandTypes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select meter band types from the list
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('bandTypes'))

    @property
    def BarrierReplyDelayType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select the Barrier Reply Delay Type
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('barrierReplyDelayType'))

    @property
    def BarrierReplyMaxDelay(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure Barrier Reply Max Delay in milli seconds.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('barrierReplyMaxDelay'))

    @property
    def Capabilities(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Capabilities
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('capabilities'))

    @property
    def ConnectedVia(self):
        """DEPRECATED 
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of layers this layer used to connect to the wire
        """
        return self._get_attribute('connectedVia')
    @ConnectedVia.setter
    def ConnectedVia(self, value):
        self._set_attribute('connectedVia', value)

    @property
    def ControllerFlowTxRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, statistics is published showing the rate at which Flows are transmitted per second, by the Controller
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('controllerFlowTxRate'))

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute('count')

    @property
    def DatapathDesc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The description of the Data Path used.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('datapathDesc'))

    @property
    def DatapathId(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Datapath ID of the OF Channel.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('datapathId'))

    @property
    def DatapathIdHex(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The Datapath ID in Hex of the OF Channel.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('datapathIdHex'))

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        """
        return self._get_attribute('descriptiveName')

    @property
    def DirectoryName(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Location of Directory in Client where the Certificate and Key Files are available
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('directoryName'))

    @property
    def EchoInterval(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The periodic interval in seconds at which the Interface sends Echo Request Packets.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('echoInterval'))

    @property
    def EchoTimeOut(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, the echo request times out when they have been sent for a specified number of times, or when the time value specified has lapsed, but no response is received
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('echoTimeOut'))

    @property
    def EnableHelloElement(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable Hello Element
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('enableHelloElement'))

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute('errors')

    @property
    def FileCaCertificate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Browse and upload a CA Certificate file for TLS session.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('fileCaCertificate'))

    @property
    def FileCertificate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Browse and upload the certificate file for TLS session.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('fileCertificate'))

    @property
    def FilePrivKey(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Browse and upload the private key file for TLS session.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('filePrivKey'))

    @property
    def FlowRemovedMask(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify the flow removed message types that will not be received when the controller has the Master role
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('flowRemovedMask'))

    @property
    def FlowRemovedMaskSlave(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify the flow removed message types that will not be received when the controller has the Slave role
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('flowRemovedMaskSlave'))

    @property
    def GroupCapabilities(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Group configuration flags: Weight:Support weight for select groups. Liveness:Support liveness for select groups. Chaining:Support chaining groups. Check Loops:Check chaining for loops and delete.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('groupCapabilities'))

    @property
    def GroupType(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Can be of the following types per switch: 1)All: Execute all buckets in the group. 2)Select:Execute one bucket in the group. 3)Indirect:Execute the one defined bucket in this group. 4)Fast Failover:Execute the first live bucket.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('groupType'))

    @property
    def HardwareDesc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The description of the hardware used.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('hardwareDesc'))

    @property
    def InterPacketInBurstGap(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify the duration (in milliseconds) for which the switch waits between successive packet-in bursts.The default value is 1,000 milliseconds.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('interPacketInBurstGap'))

    @property
    def ManufacturerDesc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The description of the manufacturer. The default value is Ixia.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('manufacturerDesc'))

    @property
    def MaxBandPerMeter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum number of bands per meter
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('maxBandPerMeter'))

    @property
    def MaxColorValue(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum Color Value
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('maxColorValue'))

    @property
    def MaxNumberOfBucketsPerGroups(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To specify the maximum number of group buckets each group can have.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('maxNumberOfBucketsPerGroups'))

    @property
    def MaxPacketInBytes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The maximum length of the Packet-in messages in bytes.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('maxPacketInBytes'))

    @property
    def MeterCapabilities(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Select meter capabilities from the list
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('meterCapabilities'))

    @property
    def Multiplier(self):
        """
        Returns
        -------
        - number: Number of layer instances per parent instance (multiplier)
        """
        return self._get_attribute('multiplier')
    @Multiplier.setter
    def Multiplier(self, value):
        self._set_attribute('multiplier', value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def NumMeter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Maximum number of Openflow meters configured for the switch
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('numMeter'))

    @property
    def NumberOfBuffers(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify the maximum number of packets the switch can buffer when sending packets to the controller using packet-in messages.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('numberOfBuffers'))

    @property
    def NumberOfChannels(self):
        """
        Returns
        -------
        - number: Total number of OpenFlow channels to be added for this protocol interface.
        """
        return self._get_attribute('numberOfChannels')
    @NumberOfChannels.setter
    def NumberOfChannels(self, value):
        self._set_attribute('numberOfChannels', value)

    @property
    def NumberOfHostPorts(self):
        """
        Returns
        -------
        - number: Number of Host Ports per Switch
        """
        return self._get_attribute('numberOfHostPorts')

    @property
    def NumberOfPacketIn(self):
        """
        Returns
        -------
        - number: Specify the number of packet-in ranges supported by the switch.The maximum allowed value is 10 ranges.
        """
        return self._get_attribute('numberOfPacketIn')
    @NumberOfPacketIn.setter
    def NumberOfPacketIn(self, value):
        self._set_attribute('numberOfPacketIn', value)

    @property
    def NumberOfPorts(self):
        """
        Returns
        -------
        - number: Number of Ports per Switch
        """
        return self._get_attribute('numberOfPorts')

    @property
    def NumberOfTableRanges(self):
        """
        Returns
        -------
        - number: Number of Tables per Switch
        """
        return self._get_attribute('numberOfTableRanges')
    @NumberOfTableRanges.setter
    def NumberOfTableRanges(self, value):
        self._set_attribute('numberOfTableRanges', value)

    @property
    def NumberOfTopologyPorts(self):
        """
        Returns
        -------
        - number: Number of Topology Ports per Switch
        """
        return self._get_attribute('numberOfTopologyPorts')

    @property
    def NumberOfUnconnectedPorts(self):
        """
        Returns
        -------
        - number: Number of Unconnected Ports per Switch
        """
        return self._get_attribute('numberOfUnconnectedPorts')
    @NumberOfUnconnectedPorts.setter
    def NumberOfUnconnectedPorts(self, value):
        self._set_attribute('numberOfUnconnectedPorts', value)

    @property
    def PacketInMaskMaster(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Packet In Mask Master
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('packetInMaskMaster'))

    @property
    def PacketInMaskSlave(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Packet In Mask Slave
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('packetInMaskSlave'))

    @property
    def PacketInReplyDelay(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, delay between packet-in and the corresponding packet-out or flow mod is published.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('packetInReplyDelay'))

    @property
    def PacketInReplyTimeout(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The amount of time, in seconds, that the switch keeps the packet-in message in buffer, if it does not receive any corresponding packet-out or flow mod.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('packetInReplyTimeout'))

    @property
    def PacketInTxBurst(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify the number of packet-in transmitting packets that can be sent in a single burst within the time frame specified by the Inter PacketIn Burst Gap value.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('packetInTxBurst'))

    @property
    def PacketOutRxRate(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, packet_out rx rate and packet_in tx rate is calculated for the switch.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('packetOutRxRate'))

    @property
    def PeriodicEcho(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, the Interface sends echo requests periodically to keep the OpenFlow session connected.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('periodicEcho'))

    @property
    def PortStatusMaskMaster(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Port Status Mask Master
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('portStatusMaskMaster'))

    @property
    def PortStatusMaskSlave(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Port Status Mask Slave
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('portStatusMaskSlave'))

    @property
    def SerialNumber(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The serial number used.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('serialNumber'))

    @property
    def SessionStatus(self):
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute('sessionStatus')

    @property
    def SoftwareDesc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The description of the software used.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('softwareDesc'))

    @property
    def StackedLayers(self):
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*]): List of secondary (many to one) child layer protocols
        """
        return self._get_attribute('stackedLayers')
    @StackedLayers.setter
    def StackedLayers(self, value):
        self._set_attribute('stackedLayers', value)

    @property
    def StateCounts(self):
        """
        Returns
        -------
        - dict(total:number,notStarted:number,down:number,up:number): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        """
        return self._get_attribute('stateCounts')

    @property
    def Status(self):
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        """
        return self._get_attribute('status')

    @property
    def StoreFlows(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, the flow information sent by the Controller are learned by the Switch.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('storeFlows'))

    @property
    def SwitchDesc(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): A description of the Switch
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('switchDesc'))

    @property
    def SwitchLocalIp(self):
        """
        Returns
        -------
        - list(str): The local IP address of the interface. This field is auto-populated and cannot be changed.
        """
        return self._get_attribute('switchLocalIp')

    @property
    def TableMissAction(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify what the Switch should do when there is no match for the packets
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('tableMissAction'))

    @property
    def TcpPort(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Specify the TCP port for this interface
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('tcpPort'))

    @property
    def TimeoutOption(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The types of timeout options supported. Choose one of the following: 1) Multiplier 2) Timeout Value
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('timeoutOption'))

    @property
    def TimeoutOptionValue(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The value specified for the selected Timeout option.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('timeoutOptionValue'))

    @property
    def TlsVersion(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): TLS version selection
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('tlsVersion'))

    @property
    def TransactionID(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): If selected, PacketIn Delay Calculation will be done by matching transaction ID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('transactionID'))

    @property
    def TypeOfConnection(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): The type of connection used for the Interface. Options include: 1) TCP 2) TLS
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('typeOfConnection'))

    @property
    def VersionSupported(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Indicates the supported OpenFlow version number.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute('versionSupported'))

    def update(self, ConnectedVia=None, Multiplier=None, Name=None, NumberOfChannels=None, NumberOfPacketIn=None, NumberOfTableRanges=None, NumberOfUnconnectedPorts=None, StackedLayers=None):
        """Updates openFlowSwitch resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfChannels (number): Total number of OpenFlow channels to be added for this protocol interface.
        - NumberOfPacketIn (number): Specify the number of packet-in ranges supported by the switch.The maximum allowed value is 10 ranges.
        - NumberOfTableRanges (number): Number of Tables per Switch
        - NumberOfUnconnectedPorts (number): Number of Unconnected Ports per Switch
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(locals())

    def add(self, ConnectedVia=None, Multiplier=None, Name=None, NumberOfChannels=None, NumberOfPacketIn=None, NumberOfTableRanges=None, NumberOfUnconnectedPorts=None, StackedLayers=None):
        """Adds a new openFlowSwitch resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfChannels (number): Total number of OpenFlow channels to be added for this protocol interface.
        - NumberOfPacketIn (number): Specify the number of packet-in ranges supported by the switch.The maximum allowed value is 10 ranges.
        - NumberOfTableRanges (number): Number of Tables per Switch
        - NumberOfUnconnectedPorts (number): Number of Unconnected Ports per Switch
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols

        Returns
        -------
        - self: This instance with all currently retrieved openFlowSwitch resources using find and the newly added openFlowSwitch resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the contained openFlowSwitch resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, ConnectedVia=None, Count=None, DescriptiveName=None, Errors=None, Multiplier=None, Name=None, NumberOfChannels=None, NumberOfHostPorts=None, NumberOfPacketIn=None, NumberOfPorts=None, NumberOfTableRanges=None, NumberOfTopologyPorts=None, NumberOfUnconnectedPorts=None, SessionStatus=None, StackedLayers=None, StateCounts=None, Status=None, SwitchLocalIp=None):
        """Finds and retrieves openFlowSwitch resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve openFlowSwitch resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all openFlowSwitch resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of layers this layer used to connect to the wire
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfChannels (number): Total number of OpenFlow channels to be added for this protocol interface.
        - NumberOfHostPorts (number): Number of Host Ports per Switch
        - NumberOfPacketIn (number): Specify the number of packet-in ranges supported by the switch.The maximum allowed value is 10 ranges.
        - NumberOfPorts (number): Number of Ports per Switch
        - NumberOfTableRanges (number): Number of Tables per Switch
        - NumberOfTopologyPorts (number): Number of Topology Ports per Switch
        - NumberOfUnconnectedPorts (number): Number of Unconnected Ports per Switch
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology/.../*])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        - SwitchLocalIp (list(str)): The local IP address of the interface. This field is auto-populated and cannot be changed.

        Returns
        -------
        - self: This instance with matching openFlowSwitch resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of openFlowSwitch data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the openFlowSwitch resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, AuxConnTimeout=None, AuxNonHelloStartupOption=None, BadVersionErrorAction=None, BandTypes=None, BarrierReplyDelayType=None, BarrierReplyMaxDelay=None, Capabilities=None, ControllerFlowTxRate=None, DatapathDesc=None, DatapathId=None, DatapathIdHex=None, DirectoryName=None, EchoInterval=None, EchoTimeOut=None, EnableHelloElement=None, FileCaCertificate=None, FileCertificate=None, FilePrivKey=None, FlowRemovedMask=None, FlowRemovedMaskSlave=None, GroupCapabilities=None, GroupType=None, HardwareDesc=None, InterPacketInBurstGap=None, ManufacturerDesc=None, MaxBandPerMeter=None, MaxColorValue=None, MaxNumberOfBucketsPerGroups=None, MaxPacketInBytes=None, MeterCapabilities=None, NumMeter=None, NumberOfBuffers=None, PacketInMaskMaster=None, PacketInMaskSlave=None, PacketInReplyDelay=None, PacketInReplyTimeout=None, PacketInTxBurst=None, PacketOutRxRate=None, PeriodicEcho=None, PortStatusMaskMaster=None, PortStatusMaskSlave=None, SerialNumber=None, SoftwareDesc=None, StoreFlows=None, SwitchDesc=None, TableMissAction=None, TcpPort=None, TimeoutOption=None, TimeoutOptionValue=None, TlsVersion=None, TransactionID=None, TypeOfConnection=None, VersionSupported=None):
        """Base class infrastructure that gets a list of openFlowSwitch device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AuxConnTimeout (str): optional regex of auxConnTimeout
        - AuxNonHelloStartupOption (str): optional regex of auxNonHelloStartupOption
        - BadVersionErrorAction (str): optional regex of badVersionErrorAction
        - BandTypes (str): optional regex of bandTypes
        - BarrierReplyDelayType (str): optional regex of barrierReplyDelayType
        - BarrierReplyMaxDelay (str): optional regex of barrierReplyMaxDelay
        - Capabilities (str): optional regex of capabilities
        - ControllerFlowTxRate (str): optional regex of controllerFlowTxRate
        - DatapathDesc (str): optional regex of datapathDesc
        - DatapathId (str): optional regex of datapathId
        - DatapathIdHex (str): optional regex of datapathIdHex
        - DirectoryName (str): optional regex of directoryName
        - EchoInterval (str): optional regex of echoInterval
        - EchoTimeOut (str): optional regex of echoTimeOut
        - EnableHelloElement (str): optional regex of enableHelloElement
        - FileCaCertificate (str): optional regex of fileCaCertificate
        - FileCertificate (str): optional regex of fileCertificate
        - FilePrivKey (str): optional regex of filePrivKey
        - FlowRemovedMask (str): optional regex of flowRemovedMask
        - FlowRemovedMaskSlave (str): optional regex of flowRemovedMaskSlave
        - GroupCapabilities (str): optional regex of groupCapabilities
        - GroupType (str): optional regex of groupType
        - HardwareDesc (str): optional regex of hardwareDesc
        - InterPacketInBurstGap (str): optional regex of interPacketInBurstGap
        - ManufacturerDesc (str): optional regex of manufacturerDesc
        - MaxBandPerMeter (str): optional regex of maxBandPerMeter
        - MaxColorValue (str): optional regex of maxColorValue
        - MaxNumberOfBucketsPerGroups (str): optional regex of maxNumberOfBucketsPerGroups
        - MaxPacketInBytes (str): optional regex of maxPacketInBytes
        - MeterCapabilities (str): optional regex of meterCapabilities
        - NumMeter (str): optional regex of numMeter
        - NumberOfBuffers (str): optional regex of numberOfBuffers
        - PacketInMaskMaster (str): optional regex of packetInMaskMaster
        - PacketInMaskSlave (str): optional regex of packetInMaskSlave
        - PacketInReplyDelay (str): optional regex of packetInReplyDelay
        - PacketInReplyTimeout (str): optional regex of packetInReplyTimeout
        - PacketInTxBurst (str): optional regex of packetInTxBurst
        - PacketOutRxRate (str): optional regex of packetOutRxRate
        - PeriodicEcho (str): optional regex of periodicEcho
        - PortStatusMaskMaster (str): optional regex of portStatusMaskMaster
        - PortStatusMaskSlave (str): optional regex of portStatusMaskSlave
        - SerialNumber (str): optional regex of serialNumber
        - SoftwareDesc (str): optional regex of softwareDesc
        - StoreFlows (str): optional regex of storeFlows
        - SwitchDesc (str): optional regex of switchDesc
        - TableMissAction (str): optional regex of tableMissAction
        - TcpPort (str): optional regex of tcpPort
        - TimeoutOption (str): optional regex of timeoutOption
        - TimeoutOptionValue (str): optional regex of timeoutOptionValue
        - TlsVersion (str): optional regex of tlsVersion
        - TransactionID (str): optional regex of transactionID
        - TypeOfConnection (str): optional regex of typeOfConnection
        - VersionSupported (str): optional regex of versionSupported

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def ClearAllLearnedInfo(self, *args, **kwargs):
        """Executes the clearAllLearnedInfo operation on the server.

        Clear OF Channels learnt by this Switch.

        clearAllLearnedInfo(Arg2=list)list
        ----------------------------------
        - Arg2 (list(number)): List of OF Channel into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('clearAllLearnedInfo', payload=payload, response_object=None)

    def GetOFChannelLearnedInfo(self, *args, **kwargs):
        """Executes the getOFChannelLearnedInfo operation on the server.

        Gets OF Channels learnt by this switch.

        getOFChannelLearnedInfo(Arg2=list)list
        --------------------------------------
        - Arg2 (list(number)): List of OF Channel into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getOFChannelLearnedInfo', payload=payload, response_object=None)

    def GetOFSwitchFlowStatLearnedInfo(self, *args, **kwargs):
        """Executes the getOFSwitchFlowStatLearnedInfo operation on the server.

        Gets OF Switch Flows learnt by this switch.

        getOFSwitchFlowStatLearnedInfo(Arg2=list)list
        ---------------------------------------------
        - Arg2 (list(number)): List of OF Switch Flows into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getOFSwitchFlowStatLearnedInfo', payload=payload, response_object=None)

    def GetOFSwitchGroupLearnedInfo(self, *args, **kwargs):
        """Executes the getOFSwitchGroupLearnedInfo operation on the server.

        Gets OF Switch Groups learnt by this switch.

        getOFSwitchGroupLearnedInfo(Arg2=list)list
        ------------------------------------------
        - Arg2 (list(number)): List of OF Switch Flows into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getOFSwitchGroupLearnedInfo', payload=payload, response_object=None)

    def GetOFSwitchMeterLearnedInfo(self, *args, **kwargs):
        """Executes the getOFSwitchMeterLearnedInfo operation on the server.

        Gets OF Switch Meter learned info for this switch.

        getOFSwitchMeterLearnedInfo(Arg2=list)list
        ------------------------------------------
        - Arg2 (list(number)): List of OF Switch Flows into the protocol plugin. An empty list indicates all instances in the plugin.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('getOFSwitchMeterLearnedInfo', payload=payload, response_object=None)

    def RestartDown(self, *args, **kwargs):
        """Executes the restartDown operation on the server.

        Stop and start interfaces and sessions that are in Down state.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        restartDown(SessionIndices=list)
        --------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

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

        Start selected protocols.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

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

        Stop selected protocols.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(SessionIndices=list)
        -------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

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
