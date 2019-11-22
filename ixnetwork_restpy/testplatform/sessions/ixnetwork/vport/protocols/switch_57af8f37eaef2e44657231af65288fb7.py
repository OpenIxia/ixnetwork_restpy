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


class Switch(Base):
    """A high level object that allows to define the switch configuration.
    The Switch class encapsulates a list of switch resources that is be managed by the user.
    A list of resources can be retrieved from the server using the Switch.find() method.
    The list can be managed by the user by using the Switch.add() and Switch.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'switch'

    def __init__(self, parent):
        super(Switch, self).__init__(parent)

    @property
    def BandTypes(self):
        """An instance of the BandTypes class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bandtypes_43eb55b1b84d828fa309ddf4c0f534ca.BandTypes)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bandtypes_43eb55b1b84d828fa309ddf4c0f534ca import BandTypes
        return BandTypes(self)._select()

    @property
    def Capabilities(self):
        """An instance of the Capabilities class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.capabilities_e80b90a1ca54950c386ad2c273e612f5.Capabilities)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.capabilities_e80b90a1ca54950c386ad2c273e612f5 import Capabilities
        return Capabilities(self)._select()

    @property
    def FlowRemovedMaskMaster(self):
        """An instance of the FlowRemovedMaskMaster class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowremovedmaskmaster_09eb9ffe579875fc78c886159c33d175.FlowRemovedMaskMaster)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowremovedmaskmaster_09eb9ffe579875fc78c886159c33d175 import FlowRemovedMaskMaster
        return FlowRemovedMaskMaster(self)._select()

    @property
    def FlowRemovedMaskSlave(self):
        """An instance of the FlowRemovedMaskSlave class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowremovedmaskslave_55710d32fe1275bb99d4ef7e02dc7d9d.FlowRemovedMaskSlave)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowremovedmaskslave_55710d32fe1275bb99d4ef7e02dc7d9d import FlowRemovedMaskSlave
        return FlowRemovedMaskSlave(self)._select()

    @property
    def GroupCapabilities(self):
        """An instance of the GroupCapabilities class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupcapabilities_406032a2e642aaa7aa3907ee76fa1c8c.GroupCapabilities)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupcapabilities_406032a2e642aaa7aa3907ee76fa1c8c import GroupCapabilities
        return GroupCapabilities(self)._select()

    @property
    def GroupTypes(self):
        """An instance of the GroupTypes class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.grouptypes_b585bcd461c8551b0ecc4fe3f6302771.GroupTypes)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.grouptypes_b585bcd461c8551b0ecc4fe3f6302771 import GroupTypes
        return GroupTypes(self)._select()

    @property
    def MeterCapabilities(self):
        """An instance of the MeterCapabilities class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.metercapabilities_fd06138d1c49a720821c1cf10537ae61.MeterCapabilities)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.metercapabilities_fd06138d1c49a720821c1cf10537ae61 import MeterCapabilities
        return MeterCapabilities(self)._select()

    @property
    def PacketInMaskMaster(self):
        """An instance of the PacketInMaskMaster class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.packetinmaskmaster_d970360e2654d4666a071d9c45097a2f.PacketInMaskMaster)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.packetinmaskmaster_d970360e2654d4666a071d9c45097a2f import PacketInMaskMaster
        return PacketInMaskMaster(self)._select()

    @property
    def PacketInMaskSlave(self):
        """An instance of the PacketInMaskSlave class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.packetinmaskslave_26c8244533f9424a1467a140c384b057.PacketInMaskSlave)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.packetinmaskslave_26c8244533f9424a1467a140c384b057 import PacketInMaskSlave
        return PacketInMaskSlave(self)._select()

    @property
    def PortStatusMaskMaster(self):
        """An instance of the PortStatusMaskMaster class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.portstatusmaskmaster_9fe7d6942f3083a0f5fbfee1386221da.PortStatusMaskMaster)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.portstatusmaskmaster_9fe7d6942f3083a0f5fbfee1386221da import PortStatusMaskMaster
        return PortStatusMaskMaster(self)._select()

    @property
    def PortStatusMaskSlave(self):
        """An instance of the PortStatusMaskSlave class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.portstatusmaskslave_f9f6a1e5a7397856a235718fd9b4a9ae.PortStatusMaskSlave)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.portstatusmaskslave_f9f6a1e5a7397856a235718fd9b4a9ae import PortStatusMaskSlave
        return PortStatusMaskSlave(self)._select()

    @property
    def SupportedActions(self):
        """An instance of the SupportedActions class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.supportedactions_b5c6c50a5a7669b03c7a3575bd7c3881.SupportedActions)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.supportedactions_b5c6c50a5a7669b03c7a3575bd7c3881 import SupportedActions
        return SupportedActions(self)._select()

    @property
    def SwitchGroupFeature(self):
        """An instance of the SwitchGroupFeature class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchgroupfeature_60f4cb9f67671315b05f4df774890f11.SwitchGroupFeature)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchgroupfeature_60f4cb9f67671315b05f4df774890f11 import SwitchGroupFeature
        return SwitchGroupFeature(self)

    @property
    def SwitchOfChannel(self):
        """An instance of the SwitchOfChannel class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchofchannel_990df5de567726917135ee08842f995f.SwitchOfChannel)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchofchannel_990df5de567726917135ee08842f995f import SwitchOfChannel
        return SwitchOfChannel(self)

    @property
    def SwitchPacketIn(self):
        """An instance of the SwitchPacketIn class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchpacketin_54d5b194bb8efd0caf25ffa7652254e4.SwitchPacketIn)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchpacketin_54d5b194bb8efd0caf25ffa7652254e4 import SwitchPacketIn
        return SwitchPacketIn(self)

    @property
    def SwitchPorts(self):
        """An instance of the SwitchPorts class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchports_aa31da616148b474429e0871a211990e.SwitchPorts)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchports_aa31da616148b474429e0871a211990e import SwitchPorts
        return SwitchPorts(self)

    @property
    def SwitchTables(self):
        """An instance of the SwitchTables class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchtables_11cbdee2b3a630627dd840c394d54a8d.SwitchTables)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchtables_11cbdee2b3a630627dd840c394d54a8d import SwitchTables
        return SwitchTables(self)

    @property
    def BarrierReplyDelay(self):
        """DEPRECATED Indicates the delay between successive barrier notifications.

        Returns:
            number
        """
        return self._get_attribute('barrierReplyDelay')
    @BarrierReplyDelay.setter
    def BarrierReplyDelay(self, value):
        self._set_attribute('barrierReplyDelay', value)

    @property
    def BarrierReplyDelayType(self):
        """Select the delay type supported for barrier reply messages

        Returns:
            str(fixed|random)
        """
        return self._get_attribute('barrierReplyDelayType')
    @BarrierReplyDelayType.setter
    def BarrierReplyDelayType(self, value):
        self._set_attribute('barrierReplyDelayType', value)

    @property
    def BarrierReplyMaxDelay(self):
        """Indicates the delay between successive barrier notifications.

        Returns:
            number
        """
        return self._get_attribute('barrierReplyMaxDelay')
    @BarrierReplyMaxDelay.setter
    def BarrierReplyMaxDelay(self, value):
        self._set_attribute('barrierReplyMaxDelay', value)

    @property
    def CalculateControllerFlowTxRate(self):
        """If true, the Flow Rate of the controller is calculated.

        Returns:
            bool
        """
        return self._get_attribute('calculateControllerFlowTxRate')
    @CalculateControllerFlowTxRate.setter
    def CalculateControllerFlowTxRate(self, value):
        self._set_attribute('calculateControllerFlowTxRate', value)

    @property
    def CalculatePacketInReplyDelay(self):
        """If true, calculates delay between Packet-In sent from Switch and reply received from Controller.

        Returns:
            bool
        """
        return self._get_attribute('calculatePacketInReplyDelay')
    @CalculatePacketInReplyDelay.setter
    def CalculatePacketInReplyDelay(self, value):
        self._set_attribute('calculatePacketInReplyDelay', value)

    @property
    def DatapathDescription(self):
        """Indicates a description of datapath.

        Returns:
            str
        """
        return self._get_attribute('datapathDescription')
    @DatapathDescription.setter
    def DatapathDescription(self, value):
        self._set_attribute('datapathDescription', value)

    @property
    def DatapathId(self):
        """Indicates the Datapath ID of the OpenFlow switch.

        Returns:
            str
        """
        return self._get_attribute('datapathId')
    @DatapathId.setter
    def DatapathId(self, value):
        self._set_attribute('datapathId', value)

    @property
    def DatapathIdInHex(self):
        """Indicates the Datapath ID in hexadecimal format.

        Returns:
            str
        """
        return self._get_attribute('datapathIdInHex')
    @DatapathIdInHex.setter
    def DatapathIdInHex(self, value):
        self._set_attribute('datapathIdInHex', value)

    @property
    def Description(self):
        """A description for the object.

        Returns:
            str
        """
        return self._get_attribute('description')
    @Description.setter
    def Description(self, value):
        self._set_attribute('description', value)

    @property
    def Enable(self):
        """If true, the object is enabled.

        Returns:
            bool
        """
        return self._get_attribute('enable')
    @Enable.setter
    def Enable(self, value):
        self._set_attribute('enable', value)

    @property
    def EnableCalculatePacketOutRxRate(self):
        """If enabled packet_out rx rate and packet_in tx rate will be caculated for the switch and shown in Aggregated Switch Statistics and Switch Learned Info. This field can be enabled only if Calculate PacketIn Reply Delay is disabled for the switch.

        Returns:
            bool
        """
        return self._get_attribute('enableCalculatePacketOutRxRate')
    @EnableCalculatePacketOutRxRate.setter
    def EnableCalculatePacketOutRxRate(self, value):
        self._set_attribute('enableCalculatePacketOutRxRate', value)

    @property
    def EnableHelloElement(self):
        """If true, enables Hello element for version negotiation.

        Returns:
            bool
        """
        return self._get_attribute('enableHelloElement')
    @EnableHelloElement.setter
    def EnableHelloElement(self, value):
        self._set_attribute('enableHelloElement', value)

    @property
    def HardwareDescription(self):
        """Indicates the hardware description of the switch.

        Returns:
            str
        """
        return self._get_attribute('hardwareDescription')
    @HardwareDescription.setter
    def HardwareDescription(self, value):
        self._set_attribute('hardwareDescription', value)

    @property
    def InterPacketInBurstGap(self):
        """Indicates the duration, in milliseconds, to wait between successive Packet-In bursts.

        Returns:
            number
        """
        return self._get_attribute('interPacketInBurstGap')
    @InterPacketInBurstGap.setter
    def InterPacketInBurstGap(self, value):
        self._set_attribute('interPacketInBurstGap', value)

    @property
    def LocalIp(self):
        """Indicates the local IP address of the interface. This field is auto-populated and cannot be changed.

        Returns:
            str
        """
        return self._get_attribute('localIp')

    @property
    def ManufacturerDescription(self):
        """Indicates the description of the switch manufacturer.

        Returns:
            str
        """
        return self._get_attribute('manufacturerDescription')
    @ManufacturerDescription.setter
    def ManufacturerDescription(self, value):
        self._set_attribute('manufacturerDescription', value)

    @property
    def MaxPacketInBytes(self):
        """Specifies the max amount of data to be sent in the Packet-In message.

        Returns:
            number
        """
        return self._get_attribute('maxPacketInBytes')
    @MaxPacketInBytes.setter
    def MaxPacketInBytes(self, value):
        self._set_attribute('maxPacketInBytes', value)

    @property
    def MaximumColorValue(self):
        """Specify the maximum color value supported.The minimum value is 0 and the maximum value is 160. The default value is 50.

        Returns:
            number
        """
        return self._get_attribute('maximumColorValue')
    @MaximumColorValue.setter
    def MaximumColorValue(self, value):
        self._set_attribute('maximumColorValue', value)

    @property
    def MaximumNoOfBandsPerMeter(self):
        """Specify the maximum number of bands supported per meter. The minimum value is 0 and the maximum value is 160. The default value is 50.

        Returns:
            number
        """
        return self._get_attribute('maximumNoOfBandsPerMeter')
    @MaximumNoOfBandsPerMeter.setter
    def MaximumNoOfBandsPerMeter(self, value):
        self._set_attribute('maximumNoOfBandsPerMeter', value)

    @property
    def MaximumNoOfBucketsPerGroup(self):
        """Specify the maximum number of Buckets supported per group.The minimum value is 1 and the maximum value is 4092.The default value is 4092.

        Returns:
            number
        """
        return self._get_attribute('maximumNoOfBucketsPerGroup')
    @MaximumNoOfBucketsPerGroup.setter
    def MaximumNoOfBucketsPerGroup(self, value):
        self._set_attribute('maximumNoOfBucketsPerGroup', value)

    @property
    def MaximumNoOfMeters(self):
        """Specify the maximum number of meters supported. The default value is 1000.

        Returns:
            number
        """
        return self._get_attribute('maximumNoOfMeters')
    @MaximumNoOfMeters.setter
    def MaximumNoOfMeters(self, value):
        self._set_attribute('maximumNoOfMeters', value)

    @property
    def NumberOfBuffers(self):
        """Indicates the maximum number of packets that can be stored in the buffered at a time.

        Returns:
            number
        """
        return self._get_attribute('numberOfBuffers')
    @NumberOfBuffers.setter
    def NumberOfBuffers(self, value):
        self._set_attribute('numberOfBuffers', value)

    @property
    def PacketInReplyTimeout(self):
        """Indicates the duration for which the Switch should wait for Packet-in-reply before freeing the buffer.

        Returns:
            number
        """
        return self._get_attribute('packetInReplyTimeout')
    @PacketInReplyTimeout.setter
    def PacketInReplyTimeout(self, value):
        self._set_attribute('packetInReplyTimeout', value)

    @property
    def PacketInTxBurstSize(self):
        """Indicates the number of packets in messages sent in a single burst.

        Returns:
            number
        """
        return self._get_attribute('packetInTxBurstSize')
    @PacketInTxBurstSize.setter
    def PacketInTxBurstSize(self, value):
        self._set_attribute('packetInTxBurstSize', value)

    @property
    def SerialNumber(self):
        """Indicates the Serial Number of the switch.

        Returns:
            str
        """
        return self._get_attribute('serialNumber')
    @SerialNumber.setter
    def SerialNumber(self, value):
        self._set_attribute('serialNumber', value)

    @property
    def SoftwareDescription(self):
        """Indicates the description of the software installed on the switch.

        Returns:
            str
        """
        return self._get_attribute('softwareDescription')
    @SoftwareDescription.setter
    def SoftwareDescription(self, value):
        self._set_attribute('softwareDescription', value)

    @property
    def StoreFlows(self):
        """If true, the switch will store the flows advertised by the controller in its tables.

        Returns:
            bool
        """
        return self._get_attribute('storeFlows')
    @StoreFlows.setter
    def StoreFlows(self, value):
        self._set_attribute('storeFlows', value)

    @property
    def SupportPacketForwarding(self):
        """If true, indicates that Packet Forwarding is supported on the OpenFlow switch.

        Returns:
            bool
        """
        return self._get_attribute('supportPacketForwarding')
    @SupportPacketForwarding.setter
    def SupportPacketForwarding(self, value):
        self._set_attribute('supportPacketForwarding', value)

    @property
    def TableMissAction(self):
        """Specify what the Switch should do when there is no match for the packets.

        Returns:
            str(drop|sendToController)
        """
        return self._get_attribute('tableMissAction')
    @TableMissAction.setter
    def TableMissAction(self, value):
        self._set_attribute('tableMissAction', value)

    def update(self, BarrierReplyDelay=None, BarrierReplyDelayType=None, BarrierReplyMaxDelay=None, CalculateControllerFlowTxRate=None, CalculatePacketInReplyDelay=None, DatapathDescription=None, DatapathId=None, DatapathIdInHex=None, Description=None, Enable=None, EnableCalculatePacketOutRxRate=None, EnableHelloElement=None, HardwareDescription=None, InterPacketInBurstGap=None, ManufacturerDescription=None, MaxPacketInBytes=None, MaximumColorValue=None, MaximumNoOfBandsPerMeter=None, MaximumNoOfBucketsPerGroup=None, MaximumNoOfMeters=None, NumberOfBuffers=None, PacketInReplyTimeout=None, PacketInTxBurstSize=None, SerialNumber=None, SoftwareDescription=None, StoreFlows=None, SupportPacketForwarding=None, TableMissAction=None):
        """Updates a child instance of switch on the server.

        Args:
            BarrierReplyDelay (number): Indicates the delay between successive barrier notifications.
            BarrierReplyDelayType (str(fixed|random)): Select the delay type supported for barrier reply messages
            BarrierReplyMaxDelay (number): Indicates the delay between successive barrier notifications.
            CalculateControllerFlowTxRate (bool): If true, the Flow Rate of the controller is calculated.
            CalculatePacketInReplyDelay (bool): If true, calculates delay between Packet-In sent from Switch and reply received from Controller.
            DatapathDescription (str): Indicates a description of datapath.
            DatapathId (str): Indicates the Datapath ID of the OpenFlow switch.
            DatapathIdInHex (str): Indicates the Datapath ID in hexadecimal format.
            Description (str): A description for the object.
            Enable (bool): If true, the object is enabled.
            EnableCalculatePacketOutRxRate (bool): If enabled packet_out rx rate and packet_in tx rate will be caculated for the switch and shown in Aggregated Switch Statistics and Switch Learned Info. This field can be enabled only if Calculate PacketIn Reply Delay is disabled for the switch.
            EnableHelloElement (bool): If true, enables Hello element for version negotiation.
            HardwareDescription (str): Indicates the hardware description of the switch.
            InterPacketInBurstGap (number): Indicates the duration, in milliseconds, to wait between successive Packet-In bursts.
            ManufacturerDescription (str): Indicates the description of the switch manufacturer.
            MaxPacketInBytes (number): Specifies the max amount of data to be sent in the Packet-In message.
            MaximumColorValue (number): Specify the maximum color value supported.The minimum value is 0 and the maximum value is 160. The default value is 50.
            MaximumNoOfBandsPerMeter (number): Specify the maximum number of bands supported per meter. The minimum value is 0 and the maximum value is 160. The default value is 50.
            MaximumNoOfBucketsPerGroup (number): Specify the maximum number of Buckets supported per group.The minimum value is 1 and the maximum value is 4092.The default value is 4092.
            MaximumNoOfMeters (number): Specify the maximum number of meters supported. The default value is 1000.
            NumberOfBuffers (number): Indicates the maximum number of packets that can be stored in the buffered at a time.
            PacketInReplyTimeout (number): Indicates the duration for which the Switch should wait for Packet-in-reply before freeing the buffer.
            PacketInTxBurstSize (number): Indicates the number of packets in messages sent in a single burst.
            SerialNumber (str): Indicates the Serial Number of the switch.
            SoftwareDescription (str): Indicates the description of the software installed on the switch.
            StoreFlows (bool): If true, the switch will store the flows advertised by the controller in its tables.
            SupportPacketForwarding (bool): If true, indicates that Packet Forwarding is supported on the OpenFlow switch.
            TableMissAction (str(drop|sendToController)): Specify what the Switch should do when there is no match for the packets.

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def add(self, BarrierReplyDelay=None, BarrierReplyDelayType=None, BarrierReplyMaxDelay=None, CalculateControllerFlowTxRate=None, CalculatePacketInReplyDelay=None, DatapathDescription=None, DatapathId=None, DatapathIdInHex=None, Description=None, Enable=None, EnableCalculatePacketOutRxRate=None, EnableHelloElement=None, HardwareDescription=None, InterPacketInBurstGap=None, ManufacturerDescription=None, MaxPacketInBytes=None, MaximumColorValue=None, MaximumNoOfBandsPerMeter=None, MaximumNoOfBucketsPerGroup=None, MaximumNoOfMeters=None, NumberOfBuffers=None, PacketInReplyTimeout=None, PacketInTxBurstSize=None, SerialNumber=None, SoftwareDescription=None, StoreFlows=None, SupportPacketForwarding=None, TableMissAction=None):
        """Adds a new switch node on the server and retrieves it in this instance.

        Args:
            BarrierReplyDelay (number): Indicates the delay between successive barrier notifications.
            BarrierReplyDelayType (str(fixed|random)): Select the delay type supported for barrier reply messages
            BarrierReplyMaxDelay (number): Indicates the delay between successive barrier notifications.
            CalculateControllerFlowTxRate (bool): If true, the Flow Rate of the controller is calculated.
            CalculatePacketInReplyDelay (bool): If true, calculates delay between Packet-In sent from Switch and reply received from Controller.
            DatapathDescription (str): Indicates a description of datapath.
            DatapathId (str): Indicates the Datapath ID of the OpenFlow switch.
            DatapathIdInHex (str): Indicates the Datapath ID in hexadecimal format.
            Description (str): A description for the object.
            Enable (bool): If true, the object is enabled.
            EnableCalculatePacketOutRxRate (bool): If enabled packet_out rx rate and packet_in tx rate will be caculated for the switch and shown in Aggregated Switch Statistics and Switch Learned Info. This field can be enabled only if Calculate PacketIn Reply Delay is disabled for the switch.
            EnableHelloElement (bool): If true, enables Hello element for version negotiation.
            HardwareDescription (str): Indicates the hardware description of the switch.
            InterPacketInBurstGap (number): Indicates the duration, in milliseconds, to wait between successive Packet-In bursts.
            ManufacturerDescription (str): Indicates the description of the switch manufacturer.
            MaxPacketInBytes (number): Specifies the max amount of data to be sent in the Packet-In message.
            MaximumColorValue (number): Specify the maximum color value supported.The minimum value is 0 and the maximum value is 160. The default value is 50.
            MaximumNoOfBandsPerMeter (number): Specify the maximum number of bands supported per meter. The minimum value is 0 and the maximum value is 160. The default value is 50.
            MaximumNoOfBucketsPerGroup (number): Specify the maximum number of Buckets supported per group.The minimum value is 1 and the maximum value is 4092.The default value is 4092.
            MaximumNoOfMeters (number): Specify the maximum number of meters supported. The default value is 1000.
            NumberOfBuffers (number): Indicates the maximum number of packets that can be stored in the buffered at a time.
            PacketInReplyTimeout (number): Indicates the duration for which the Switch should wait for Packet-in-reply before freeing the buffer.
            PacketInTxBurstSize (number): Indicates the number of packets in messages sent in a single burst.
            SerialNumber (str): Indicates the Serial Number of the switch.
            SoftwareDescription (str): Indicates the description of the software installed on the switch.
            StoreFlows (bool): If true, the switch will store the flows advertised by the controller in its tables.
            SupportPacketForwarding (bool): If true, indicates that Packet Forwarding is supported on the OpenFlow switch.
            TableMissAction (str(drop|sendToController)): Specify what the Switch should do when there is no match for the packets.

        Returns:
            self: This instance with all currently retrieved switch data using find and the newly added switch data available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(locals())

    def remove(self):
        """Deletes all the switch data in this instance from server.

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, BarrierReplyDelay=None, BarrierReplyDelayType=None, BarrierReplyMaxDelay=None, CalculateControllerFlowTxRate=None, CalculatePacketInReplyDelay=None, DatapathDescription=None, DatapathId=None, DatapathIdInHex=None, Description=None, Enable=None, EnableCalculatePacketOutRxRate=None, EnableHelloElement=None, HardwareDescription=None, InterPacketInBurstGap=None, LocalIp=None, ManufacturerDescription=None, MaxPacketInBytes=None, MaximumColorValue=None, MaximumNoOfBandsPerMeter=None, MaximumNoOfBucketsPerGroup=None, MaximumNoOfMeters=None, NumberOfBuffers=None, PacketInReplyTimeout=None, PacketInTxBurstSize=None, SerialNumber=None, SoftwareDescription=None, StoreFlows=None, SupportPacketForwarding=None, TableMissAction=None):
        """Finds and retrieves switch data from the server.

        All named parameters support regex and can be used to selectively retrieve switch data from the server.
        By default the find method takes no parameters and will retrieve all switch data from the server.

        Args:
            BarrierReplyDelay (number): Indicates the delay between successive barrier notifications.
            BarrierReplyDelayType (str(fixed|random)): Select the delay type supported for barrier reply messages
            BarrierReplyMaxDelay (number): Indicates the delay between successive barrier notifications.
            CalculateControllerFlowTxRate (bool): If true, the Flow Rate of the controller is calculated.
            CalculatePacketInReplyDelay (bool): If true, calculates delay between Packet-In sent from Switch and reply received from Controller.
            DatapathDescription (str): Indicates a description of datapath.
            DatapathId (str): Indicates the Datapath ID of the OpenFlow switch.
            DatapathIdInHex (str): Indicates the Datapath ID in hexadecimal format.
            Description (str): A description for the object.
            Enable (bool): If true, the object is enabled.
            EnableCalculatePacketOutRxRate (bool): If enabled packet_out rx rate and packet_in tx rate will be caculated for the switch and shown in Aggregated Switch Statistics and Switch Learned Info. This field can be enabled only if Calculate PacketIn Reply Delay is disabled for the switch.
            EnableHelloElement (bool): If true, enables Hello element for version negotiation.
            HardwareDescription (str): Indicates the hardware description of the switch.
            InterPacketInBurstGap (number): Indicates the duration, in milliseconds, to wait between successive Packet-In bursts.
            LocalIp (str): Indicates the local IP address of the interface. This field is auto-populated and cannot be changed.
            ManufacturerDescription (str): Indicates the description of the switch manufacturer.
            MaxPacketInBytes (number): Specifies the max amount of data to be sent in the Packet-In message.
            MaximumColorValue (number): Specify the maximum color value supported.The minimum value is 0 and the maximum value is 160. The default value is 50.
            MaximumNoOfBandsPerMeter (number): Specify the maximum number of bands supported per meter. The minimum value is 0 and the maximum value is 160. The default value is 50.
            MaximumNoOfBucketsPerGroup (number): Specify the maximum number of Buckets supported per group.The minimum value is 1 and the maximum value is 4092.The default value is 4092.
            MaximumNoOfMeters (number): Specify the maximum number of meters supported. The default value is 1000.
            NumberOfBuffers (number): Indicates the maximum number of packets that can be stored in the buffered at a time.
            PacketInReplyTimeout (number): Indicates the duration for which the Switch should wait for Packet-in-reply before freeing the buffer.
            PacketInTxBurstSize (number): Indicates the number of packets in messages sent in a single burst.
            SerialNumber (str): Indicates the Serial Number of the switch.
            SoftwareDescription (str): Indicates the description of the software installed on the switch.
            StoreFlows (bool): If true, the switch will store the flows advertised by the controller in its tables.
            SupportPacketForwarding (bool): If true, indicates that Packet Forwarding is supported on the OpenFlow switch.
            TableMissAction (str(drop|sendToController)): Specify what the Switch should do when there is no match for the packets.

        Returns:
            self: This instance with matching switch data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of switch data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the switch data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
