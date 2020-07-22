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


class Switch(Base):
    """A high level object that allows to define the switch configuration.
    The Switch class encapsulates a list of switch resources that are managed by the user.
    A list of resources can be retrieved from the server using the Switch.find() method.
    The list can be managed by using the Switch.add() and Switch.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'switch'
    _SDM_ATT_MAP = {
        'BarrierReplyDelay': 'barrierReplyDelay',
        'BarrierReplyDelayType': 'barrierReplyDelayType',
        'BarrierReplyMaxDelay': 'barrierReplyMaxDelay',
        'CalculateControllerFlowTxRate': 'calculateControllerFlowTxRate',
        'CalculatePacketInReplyDelay': 'calculatePacketInReplyDelay',
        'DatapathDescription': 'datapathDescription',
        'DatapathId': 'datapathId',
        'DatapathIdInHex': 'datapathIdInHex',
        'Description': 'description',
        'Enable': 'enable',
        'EnableCalculatePacketOutRxRate': 'enableCalculatePacketOutRxRate',
        'EnableHelloElement': 'enableHelloElement',
        'HardwareDescription': 'hardwareDescription',
        'InterPacketInBurstGap': 'interPacketInBurstGap',
        'LocalIp': 'localIp',
        'ManufacturerDescription': 'manufacturerDescription',
        'MaxPacketInBytes': 'maxPacketInBytes',
        'MaximumColorValue': 'maximumColorValue',
        'MaximumNoOfBandsPerMeter': 'maximumNoOfBandsPerMeter',
        'MaximumNoOfBucketsPerGroup': 'maximumNoOfBucketsPerGroup',
        'MaximumNoOfMeters': 'maximumNoOfMeters',
        'NumberOfBuffers': 'numberOfBuffers',
        'PacketInReplyTimeout': 'packetInReplyTimeout',
        'PacketInTxBurstSize': 'packetInTxBurstSize',
        'SerialNumber': 'serialNumber',
        'SoftwareDescription': 'softwareDescription',
        'StoreFlows': 'storeFlows',
        'SupportPacketForwarding': 'supportPacketForwarding',
        'TableMissAction': 'tableMissAction',
    }

    def __init__(self, parent):
        super(Switch, self).__init__(parent)

    @property
    def BandTypes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bandtypes_ac14d6ae7ec92cc37d27a3f601ff4b3e.BandTypes): An instance of the BandTypes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.bandtypes_ac14d6ae7ec92cc37d27a3f601ff4b3e import BandTypes
        return BandTypes(self)._select()

    @property
    def Capabilities(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.capabilities_e34fedc02893b4ebddb7e5f9d242efcc.Capabilities): An instance of the Capabilities class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.capabilities_e34fedc02893b4ebddb7e5f9d242efcc import Capabilities
        return Capabilities(self)._select()

    @property
    def FlowRemovedMaskMaster(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowremovedmaskmaster_2522f3935afb5408b7c450b266ff2116.FlowRemovedMaskMaster): An instance of the FlowRemovedMaskMaster class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowremovedmaskmaster_2522f3935afb5408b7c450b266ff2116 import FlowRemovedMaskMaster
        return FlowRemovedMaskMaster(self)._select()

    @property
    def FlowRemovedMaskSlave(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowremovedmaskslave_24c41ab64449f7295d6dd3b1e414b200.FlowRemovedMaskSlave): An instance of the FlowRemovedMaskSlave class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowremovedmaskslave_24c41ab64449f7295d6dd3b1e414b200 import FlowRemovedMaskSlave
        return FlowRemovedMaskSlave(self)._select()

    @property
    def GroupCapabilities(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupcapabilities_2d2cf5a25783fc63572f4750898f0ffb.GroupCapabilities): An instance of the GroupCapabilities class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.groupcapabilities_2d2cf5a25783fc63572f4750898f0ffb import GroupCapabilities
        return GroupCapabilities(self)._select()

    @property
    def GroupTypes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.grouptypes_0e0308131f27031abb2397531089069f.GroupTypes): An instance of the GroupTypes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.grouptypes_0e0308131f27031abb2397531089069f import GroupTypes
        return GroupTypes(self)._select()

    @property
    def MeterCapabilities(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.metercapabilities_1f778f8f76de1897a3e28f85e6a8a3f2.MeterCapabilities): An instance of the MeterCapabilities class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.metercapabilities_1f778f8f76de1897a3e28f85e6a8a3f2 import MeterCapabilities
        return MeterCapabilities(self)._select()

    @property
    def PacketInMaskMaster(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.packetinmaskmaster_856bc052c2c2e0d9c4040a29e033f8db.PacketInMaskMaster): An instance of the PacketInMaskMaster class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.packetinmaskmaster_856bc052c2c2e0d9c4040a29e033f8db import PacketInMaskMaster
        return PacketInMaskMaster(self)._select()

    @property
    def PacketInMaskSlave(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.packetinmaskslave_8ba122a606aac86ac72959a685bc4107.PacketInMaskSlave): An instance of the PacketInMaskSlave class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.packetinmaskslave_8ba122a606aac86ac72959a685bc4107 import PacketInMaskSlave
        return PacketInMaskSlave(self)._select()

    @property
    def PortStatusMaskMaster(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.portstatusmaskmaster_74d74bdc240320eb465b447e209efad6.PortStatusMaskMaster): An instance of the PortStatusMaskMaster class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.portstatusmaskmaster_74d74bdc240320eb465b447e209efad6 import PortStatusMaskMaster
        return PortStatusMaskMaster(self)._select()

    @property
    def PortStatusMaskSlave(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.portstatusmaskslave_f86ba2ffbe12ce5efe30759e1ff9275e.PortStatusMaskSlave): An instance of the PortStatusMaskSlave class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.portstatusmaskslave_f86ba2ffbe12ce5efe30759e1ff9275e import PortStatusMaskSlave
        return PortStatusMaskSlave(self)._select()

    @property
    def SupportedActions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.supportedactions_254a680c00e984c339218013d4bba199.SupportedActions): An instance of the SupportedActions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.supportedactions_254a680c00e984c339218013d4bba199 import SupportedActions
        return SupportedActions(self)._select()

    @property
    def SwitchGroupFeature(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchgroupfeature_47c69e96862f313a7efa2b2e5eefd71f.SwitchGroupFeature): An instance of the SwitchGroupFeature class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchgroupfeature_47c69e96862f313a7efa2b2e5eefd71f import SwitchGroupFeature
        return SwitchGroupFeature(self)

    @property
    def SwitchOfChannel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchofchannel_81cafa8215eef199c796f8a41ade2b4b.SwitchOfChannel): An instance of the SwitchOfChannel class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchofchannel_81cafa8215eef199c796f8a41ade2b4b import SwitchOfChannel
        return SwitchOfChannel(self)

    @property
    def SwitchPacketIn(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchpacketin_2bf8b0ff1576e2d6e9f42eca185b98c8.SwitchPacketIn): An instance of the SwitchPacketIn class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchpacketin_2bf8b0ff1576e2d6e9f42eca185b98c8 import SwitchPacketIn
        return SwitchPacketIn(self)

    @property
    def SwitchPorts(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchports_f5ed295522ded3b657e02bfad603b64c.SwitchPorts): An instance of the SwitchPorts class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchports_f5ed295522ded3b657e02bfad603b64c import SwitchPorts
        return SwitchPorts(self)

    @property
    def SwitchTables(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchtables_be69a28d9f70488cc5f1e497740e8fd5.SwitchTables): An instance of the SwitchTables class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchtables_be69a28d9f70488cc5f1e497740e8fd5 import SwitchTables
        return SwitchTables(self)

    @property
    def BarrierReplyDelay(self):
        """DEPRECATED 
        Returns
        -------
        - number: Indicates the delay between successive barrier notifications.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BarrierReplyDelay'])
    @BarrierReplyDelay.setter
    def BarrierReplyDelay(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BarrierReplyDelay'], value)

    @property
    def BarrierReplyDelayType(self):
        """
        Returns
        -------
        - str(fixed | random): Select the delay type supported for barrier reply messages
        """
        return self._get_attribute(self._SDM_ATT_MAP['BarrierReplyDelayType'])
    @BarrierReplyDelayType.setter
    def BarrierReplyDelayType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BarrierReplyDelayType'], value)

    @property
    def BarrierReplyMaxDelay(self):
        """
        Returns
        -------
        - number: Indicates the delay between successive barrier notifications.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BarrierReplyMaxDelay'])
    @BarrierReplyMaxDelay.setter
    def BarrierReplyMaxDelay(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BarrierReplyMaxDelay'], value)

    @property
    def CalculateControllerFlowTxRate(self):
        """
        Returns
        -------
        - bool: If true, the Flow Rate of the controller is calculated.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CalculateControllerFlowTxRate'])
    @CalculateControllerFlowTxRate.setter
    def CalculateControllerFlowTxRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CalculateControllerFlowTxRate'], value)

    @property
    def CalculatePacketInReplyDelay(self):
        """
        Returns
        -------
        - bool: If true, calculates delay between Packet-In sent from Switch and reply received from Controller.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CalculatePacketInReplyDelay'])
    @CalculatePacketInReplyDelay.setter
    def CalculatePacketInReplyDelay(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CalculatePacketInReplyDelay'], value)

    @property
    def DatapathDescription(self):
        """
        Returns
        -------
        - str: Indicates a description of datapath.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DatapathDescription'])
    @DatapathDescription.setter
    def DatapathDescription(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DatapathDescription'], value)

    @property
    def DatapathId(self):
        """
        Returns
        -------
        - str: Indicates the Datapath ID of the OpenFlow switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DatapathId'])
    @DatapathId.setter
    def DatapathId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DatapathId'], value)

    @property
    def DatapathIdInHex(self):
        """
        Returns
        -------
        - str: Indicates the Datapath ID in hexadecimal format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DatapathIdInHex'])
    @DatapathIdInHex.setter
    def DatapathIdInHex(self, value):
        self._set_attribute(self._SDM_ATT_MAP['DatapathIdInHex'], value)

    @property
    def Description(self):
        """
        Returns
        -------
        - str: A description for the object.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Description'])
    @Description.setter
    def Description(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Description'], value)

    @property
    def Enable(self):
        """
        Returns
        -------
        - bool: If true, the object is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enable'])
    @Enable.setter
    def Enable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enable'], value)

    @property
    def EnableCalculatePacketOutRxRate(self):
        """
        Returns
        -------
        - bool: If enabled packet_out rx rate and packet_in tx rate will be caculated for the switch and shown in Aggregated Switch Statistics and Switch Learned Info. This field can be enabled only if Calculate PacketIn Reply Delay is disabled for the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableCalculatePacketOutRxRate'])
    @EnableCalculatePacketOutRxRate.setter
    def EnableCalculatePacketOutRxRate(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableCalculatePacketOutRxRate'], value)

    @property
    def EnableHelloElement(self):
        """
        Returns
        -------
        - bool: If true, enables Hello element for version negotiation.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableHelloElement'])
    @EnableHelloElement.setter
    def EnableHelloElement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableHelloElement'], value)

    @property
    def HardwareDescription(self):
        """
        Returns
        -------
        - str: Indicates the hardware description of the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HardwareDescription'])
    @HardwareDescription.setter
    def HardwareDescription(self, value):
        self._set_attribute(self._SDM_ATT_MAP['HardwareDescription'], value)

    @property
    def InterPacketInBurstGap(self):
        """
        Returns
        -------
        - number: Indicates the duration, in milliseconds, to wait between successive Packet-In bursts.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterPacketInBurstGap'])
    @InterPacketInBurstGap.setter
    def InterPacketInBurstGap(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterPacketInBurstGap'], value)

    @property
    def LocalIp(self):
        """
        Returns
        -------
        - str: Indicates the local IP address of the interface. This field is auto-populated and cannot be changed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalIp'])

    @property
    def ManufacturerDescription(self):
        """
        Returns
        -------
        - str: Indicates the description of the switch manufacturer.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ManufacturerDescription'])
    @ManufacturerDescription.setter
    def ManufacturerDescription(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ManufacturerDescription'], value)

    @property
    def MaxPacketInBytes(self):
        """
        Returns
        -------
        - number: Specifies the max amount of data to be sent in the Packet-In message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaxPacketInBytes'])
    @MaxPacketInBytes.setter
    def MaxPacketInBytes(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaxPacketInBytes'], value)

    @property
    def MaximumColorValue(self):
        """
        Returns
        -------
        - number: Specify the maximum color value supported.The minimum value is 0 and the maximum value is 160. The default value is 50.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaximumColorValue'])
    @MaximumColorValue.setter
    def MaximumColorValue(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaximumColorValue'], value)

    @property
    def MaximumNoOfBandsPerMeter(self):
        """
        Returns
        -------
        - number: Specify the maximum number of bands supported per meter. The minimum value is 0 and the maximum value is 160. The default value is 50.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaximumNoOfBandsPerMeter'])
    @MaximumNoOfBandsPerMeter.setter
    def MaximumNoOfBandsPerMeter(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaximumNoOfBandsPerMeter'], value)

    @property
    def MaximumNoOfBucketsPerGroup(self):
        """
        Returns
        -------
        - number: Specify the maximum number of Buckets supported per group.The minimum value is 1 and the maximum value is 4092.The default value is 4092.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaximumNoOfBucketsPerGroup'])
    @MaximumNoOfBucketsPerGroup.setter
    def MaximumNoOfBucketsPerGroup(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaximumNoOfBucketsPerGroup'], value)

    @property
    def MaximumNoOfMeters(self):
        """
        Returns
        -------
        - number: Specify the maximum number of meters supported. The default value is 1000.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaximumNoOfMeters'])
    @MaximumNoOfMeters.setter
    def MaximumNoOfMeters(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MaximumNoOfMeters'], value)

    @property
    def NumberOfBuffers(self):
        """
        Returns
        -------
        - number: Indicates the maximum number of packets that can be stored in the buffered at a time.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfBuffers'])
    @NumberOfBuffers.setter
    def NumberOfBuffers(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfBuffers'], value)

    @property
    def PacketInReplyTimeout(self):
        """
        Returns
        -------
        - number: Indicates the duration for which the Switch should wait for Packet-in-reply before freeing the buffer.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketInReplyTimeout'])
    @PacketInReplyTimeout.setter
    def PacketInReplyTimeout(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PacketInReplyTimeout'], value)

    @property
    def PacketInTxBurstSize(self):
        """
        Returns
        -------
        - number: Indicates the number of packets in messages sent in a single burst.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketInTxBurstSize'])
    @PacketInTxBurstSize.setter
    def PacketInTxBurstSize(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PacketInTxBurstSize'], value)

    @property
    def SerialNumber(self):
        """
        Returns
        -------
        - str: Indicates the Serial Number of the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SerialNumber'])
    @SerialNumber.setter
    def SerialNumber(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SerialNumber'], value)

    @property
    def SoftwareDescription(self):
        """
        Returns
        -------
        - str: Indicates the description of the software installed on the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SoftwareDescription'])
    @SoftwareDescription.setter
    def SoftwareDescription(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SoftwareDescription'], value)

    @property
    def StoreFlows(self):
        """
        Returns
        -------
        - bool: If true, the switch will store the flows advertised by the controller in its tables.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StoreFlows'])
    @StoreFlows.setter
    def StoreFlows(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StoreFlows'], value)

    @property
    def SupportPacketForwarding(self):
        """
        Returns
        -------
        - bool: If true, indicates that Packet Forwarding is supported on the OpenFlow switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SupportPacketForwarding'])
    @SupportPacketForwarding.setter
    def SupportPacketForwarding(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SupportPacketForwarding'], value)

    @property
    def TableMissAction(self):
        """
        Returns
        -------
        - str(drop | sendToController): Specify what the Switch should do when there is no match for the packets.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TableMissAction'])
    @TableMissAction.setter
    def TableMissAction(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TableMissAction'], value)

    def update(self, BarrierReplyDelay=None, BarrierReplyDelayType=None, BarrierReplyMaxDelay=None, CalculateControllerFlowTxRate=None, CalculatePacketInReplyDelay=None, DatapathDescription=None, DatapathId=None, DatapathIdInHex=None, Description=None, Enable=None, EnableCalculatePacketOutRxRate=None, EnableHelloElement=None, HardwareDescription=None, InterPacketInBurstGap=None, ManufacturerDescription=None, MaxPacketInBytes=None, MaximumColorValue=None, MaximumNoOfBandsPerMeter=None, MaximumNoOfBucketsPerGroup=None, MaximumNoOfMeters=None, NumberOfBuffers=None, PacketInReplyTimeout=None, PacketInTxBurstSize=None, SerialNumber=None, SoftwareDescription=None, StoreFlows=None, SupportPacketForwarding=None, TableMissAction=None):
        """Updates switch resource on the server.

        Args
        ----
        - BarrierReplyDelay (number): Indicates the delay between successive barrier notifications.
        - BarrierReplyDelayType (str(fixed | random)): Select the delay type supported for barrier reply messages
        - BarrierReplyMaxDelay (number): Indicates the delay between successive barrier notifications.
        - CalculateControllerFlowTxRate (bool): If true, the Flow Rate of the controller is calculated.
        - CalculatePacketInReplyDelay (bool): If true, calculates delay between Packet-In sent from Switch and reply received from Controller.
        - DatapathDescription (str): Indicates a description of datapath.
        - DatapathId (str): Indicates the Datapath ID of the OpenFlow switch.
        - DatapathIdInHex (str): Indicates the Datapath ID in hexadecimal format.
        - Description (str): A description for the object.
        - Enable (bool): If true, the object is enabled.
        - EnableCalculatePacketOutRxRate (bool): If enabled packet_out rx rate and packet_in tx rate will be caculated for the switch and shown in Aggregated Switch Statistics and Switch Learned Info. This field can be enabled only if Calculate PacketIn Reply Delay is disabled for the switch.
        - EnableHelloElement (bool): If true, enables Hello element for version negotiation.
        - HardwareDescription (str): Indicates the hardware description of the switch.
        - InterPacketInBurstGap (number): Indicates the duration, in milliseconds, to wait between successive Packet-In bursts.
        - ManufacturerDescription (str): Indicates the description of the switch manufacturer.
        - MaxPacketInBytes (number): Specifies the max amount of data to be sent in the Packet-In message.
        - MaximumColorValue (number): Specify the maximum color value supported.The minimum value is 0 and the maximum value is 160. The default value is 50.
        - MaximumNoOfBandsPerMeter (number): Specify the maximum number of bands supported per meter. The minimum value is 0 and the maximum value is 160. The default value is 50.
        - MaximumNoOfBucketsPerGroup (number): Specify the maximum number of Buckets supported per group.The minimum value is 1 and the maximum value is 4092.The default value is 4092.
        - MaximumNoOfMeters (number): Specify the maximum number of meters supported. The default value is 1000.
        - NumberOfBuffers (number): Indicates the maximum number of packets that can be stored in the buffered at a time.
        - PacketInReplyTimeout (number): Indicates the duration for which the Switch should wait for Packet-in-reply before freeing the buffer.
        - PacketInTxBurstSize (number): Indicates the number of packets in messages sent in a single burst.
        - SerialNumber (str): Indicates the Serial Number of the switch.
        - SoftwareDescription (str): Indicates the description of the software installed on the switch.
        - StoreFlows (bool): If true, the switch will store the flows advertised by the controller in its tables.
        - SupportPacketForwarding (bool): If true, indicates that Packet Forwarding is supported on the OpenFlow switch.
        - TableMissAction (str(drop | sendToController)): Specify what the Switch should do when there is no match for the packets.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, BarrierReplyDelay=None, BarrierReplyDelayType=None, BarrierReplyMaxDelay=None, CalculateControllerFlowTxRate=None, CalculatePacketInReplyDelay=None, DatapathDescription=None, DatapathId=None, DatapathIdInHex=None, Description=None, Enable=None, EnableCalculatePacketOutRxRate=None, EnableHelloElement=None, HardwareDescription=None, InterPacketInBurstGap=None, ManufacturerDescription=None, MaxPacketInBytes=None, MaximumColorValue=None, MaximumNoOfBandsPerMeter=None, MaximumNoOfBucketsPerGroup=None, MaximumNoOfMeters=None, NumberOfBuffers=None, PacketInReplyTimeout=None, PacketInTxBurstSize=None, SerialNumber=None, SoftwareDescription=None, StoreFlows=None, SupportPacketForwarding=None, TableMissAction=None):
        """Adds a new switch resource on the server and adds it to the container.

        Args
        ----
        - BarrierReplyDelay (number): Indicates the delay between successive barrier notifications.
        - BarrierReplyDelayType (str(fixed | random)): Select the delay type supported for barrier reply messages
        - BarrierReplyMaxDelay (number): Indicates the delay between successive barrier notifications.
        - CalculateControllerFlowTxRate (bool): If true, the Flow Rate of the controller is calculated.
        - CalculatePacketInReplyDelay (bool): If true, calculates delay between Packet-In sent from Switch and reply received from Controller.
        - DatapathDescription (str): Indicates a description of datapath.
        - DatapathId (str): Indicates the Datapath ID of the OpenFlow switch.
        - DatapathIdInHex (str): Indicates the Datapath ID in hexadecimal format.
        - Description (str): A description for the object.
        - Enable (bool): If true, the object is enabled.
        - EnableCalculatePacketOutRxRate (bool): If enabled packet_out rx rate and packet_in tx rate will be caculated for the switch and shown in Aggregated Switch Statistics and Switch Learned Info. This field can be enabled only if Calculate PacketIn Reply Delay is disabled for the switch.
        - EnableHelloElement (bool): If true, enables Hello element for version negotiation.
        - HardwareDescription (str): Indicates the hardware description of the switch.
        - InterPacketInBurstGap (number): Indicates the duration, in milliseconds, to wait between successive Packet-In bursts.
        - ManufacturerDescription (str): Indicates the description of the switch manufacturer.
        - MaxPacketInBytes (number): Specifies the max amount of data to be sent in the Packet-In message.
        - MaximumColorValue (number): Specify the maximum color value supported.The minimum value is 0 and the maximum value is 160. The default value is 50.
        - MaximumNoOfBandsPerMeter (number): Specify the maximum number of bands supported per meter. The minimum value is 0 and the maximum value is 160. The default value is 50.
        - MaximumNoOfBucketsPerGroup (number): Specify the maximum number of Buckets supported per group.The minimum value is 1 and the maximum value is 4092.The default value is 4092.
        - MaximumNoOfMeters (number): Specify the maximum number of meters supported. The default value is 1000.
        - NumberOfBuffers (number): Indicates the maximum number of packets that can be stored in the buffered at a time.
        - PacketInReplyTimeout (number): Indicates the duration for which the Switch should wait for Packet-in-reply before freeing the buffer.
        - PacketInTxBurstSize (number): Indicates the number of packets in messages sent in a single burst.
        - SerialNumber (str): Indicates the Serial Number of the switch.
        - SoftwareDescription (str): Indicates the description of the software installed on the switch.
        - StoreFlows (bool): If true, the switch will store the flows advertised by the controller in its tables.
        - SupportPacketForwarding (bool): If true, indicates that Packet Forwarding is supported on the OpenFlow switch.
        - TableMissAction (str(drop | sendToController)): Specify what the Switch should do when there is no match for the packets.

        Returns
        -------
        - self: This instance with all currently retrieved switch resources using find and the newly added switch resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained switch resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, BarrierReplyDelay=None, BarrierReplyDelayType=None, BarrierReplyMaxDelay=None, CalculateControllerFlowTxRate=None, CalculatePacketInReplyDelay=None, DatapathDescription=None, DatapathId=None, DatapathIdInHex=None, Description=None, Enable=None, EnableCalculatePacketOutRxRate=None, EnableHelloElement=None, HardwareDescription=None, InterPacketInBurstGap=None, LocalIp=None, ManufacturerDescription=None, MaxPacketInBytes=None, MaximumColorValue=None, MaximumNoOfBandsPerMeter=None, MaximumNoOfBucketsPerGroup=None, MaximumNoOfMeters=None, NumberOfBuffers=None, PacketInReplyTimeout=None, PacketInTxBurstSize=None, SerialNumber=None, SoftwareDescription=None, StoreFlows=None, SupportPacketForwarding=None, TableMissAction=None):
        """Finds and retrieves switch resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve switch resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all switch resources from the server.

        Args
        ----
        - BarrierReplyDelay (number): Indicates the delay between successive barrier notifications.
        - BarrierReplyDelayType (str(fixed | random)): Select the delay type supported for barrier reply messages
        - BarrierReplyMaxDelay (number): Indicates the delay between successive barrier notifications.
        - CalculateControllerFlowTxRate (bool): If true, the Flow Rate of the controller is calculated.
        - CalculatePacketInReplyDelay (bool): If true, calculates delay between Packet-In sent from Switch and reply received from Controller.
        - DatapathDescription (str): Indicates a description of datapath.
        - DatapathId (str): Indicates the Datapath ID of the OpenFlow switch.
        - DatapathIdInHex (str): Indicates the Datapath ID in hexadecimal format.
        - Description (str): A description for the object.
        - Enable (bool): If true, the object is enabled.
        - EnableCalculatePacketOutRxRate (bool): If enabled packet_out rx rate and packet_in tx rate will be caculated for the switch and shown in Aggregated Switch Statistics and Switch Learned Info. This field can be enabled only if Calculate PacketIn Reply Delay is disabled for the switch.
        - EnableHelloElement (bool): If true, enables Hello element for version negotiation.
        - HardwareDescription (str): Indicates the hardware description of the switch.
        - InterPacketInBurstGap (number): Indicates the duration, in milliseconds, to wait between successive Packet-In bursts.
        - LocalIp (str): Indicates the local IP address of the interface. This field is auto-populated and cannot be changed.
        - ManufacturerDescription (str): Indicates the description of the switch manufacturer.
        - MaxPacketInBytes (number): Specifies the max amount of data to be sent in the Packet-In message.
        - MaximumColorValue (number): Specify the maximum color value supported.The minimum value is 0 and the maximum value is 160. The default value is 50.
        - MaximumNoOfBandsPerMeter (number): Specify the maximum number of bands supported per meter. The minimum value is 0 and the maximum value is 160. The default value is 50.
        - MaximumNoOfBucketsPerGroup (number): Specify the maximum number of Buckets supported per group.The minimum value is 1 and the maximum value is 4092.The default value is 4092.
        - MaximumNoOfMeters (number): Specify the maximum number of meters supported. The default value is 1000.
        - NumberOfBuffers (number): Indicates the maximum number of packets that can be stored in the buffered at a time.
        - PacketInReplyTimeout (number): Indicates the duration for which the Switch should wait for Packet-in-reply before freeing the buffer.
        - PacketInTxBurstSize (number): Indicates the number of packets in messages sent in a single burst.
        - SerialNumber (str): Indicates the Serial Number of the switch.
        - SoftwareDescription (str): Indicates the description of the software installed on the switch.
        - StoreFlows (bool): If true, the switch will store the flows advertised by the controller in its tables.
        - SupportPacketForwarding (bool): If true, indicates that Packet Forwarding is supported on the OpenFlow switch.
        - TableMissAction (str(drop | sendToController)): Specify what the Switch should do when there is no match for the packets.

        Returns
        -------
        - self: This instance with matching switch resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of switch data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the switch resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
