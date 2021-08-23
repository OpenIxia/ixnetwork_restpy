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
from typing import List, Any, Union


class OfChannel(Base):
    """Signifies the OF Channel used in this protocol configuration.
    The OfChannel class encapsulates a list of ofChannel resources that are managed by the user.
    A list of resources can be retrieved from the server using the OfChannel.find() method.
    The list can be managed by using the OfChannel.add() and OfChannel.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ofChannel'
    _SDM_ATT_MAP = {
        'CalculateFlows': 'calculateFlows',
        'CalculatePacketInReplyDelay': 'calculatePacketInReplyDelay',
        'DataPathId': 'dataPathId',
        'DataPathIdInHex': 'dataPathIdInHex',
        'DatapathDescritpion': 'datapathDescritpion',
        'Description': 'description',
        'EnableCalculateFlowsPerSecondUsingBarrierReq': 'enableCalculateFlowsPerSecondUsingBarrierReq',
        'EnableHelloElement': 'enableHelloElement',
        'EnableStartupEmptyTableFeatureRequest': 'enableStartupEmptyTableFeatureRequest',
        'Enabled': 'enabled',
        'FlowTxBurstSize': 'flowTxBurstSize',
        'HardwareDescription': 'hardwareDescription',
        'InterFlowBurstGap': 'interFlowBurstGap',
        'InterPacketInBurstGap': 'interPacketInBurstGap',
        'LocalIp': 'localIp',
        'ManufacturerDescription': 'manufacturerDescription',
        'MaximumNumberOfFlowsProcessed': 'maximumNumberOfFlowsProcessed',
        'MaximumPacketInBytes': 'maximumPacketInBytes',
        'NumberOfBuffers': 'numberOfBuffers',
        'PacketInReplyTimeout': 'packetInReplyTimeout',
        'PacketInTxBurstSize': 'packetInTxBurstSize',
        'RemoteIp': 'remoteIp',
        'SerialNumber': 'serialNumber',
        'SoftwareDescription': 'softwareDescription',
        'StartUpGenerationId': 'startUpGenerationId',
        'StartUpRoleRequest': 'startUpRoleRequest',
        'StartupFeatureRequest': 'startupFeatureRequest',
        'StoreFlows': 'storeFlows',
        'UseDataPathIdAsChannelIdentifier': 'useDataPathIdAsChannelIdentifier',
        'UseDatapathId': 'useDatapathId',
    }
    _SDM_ENUM_MAP = {
        'startUpRoleRequest': ['noRoleRequest', 'master', 'slave'],
    }

    def __init__(self, parent, list_op=False):
        super(OfChannel, self).__init__(parent, list_op)

    @property
    def Capabilities(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.capabilities_4b75c5667348309f05b3d70410a39ec1.Capabilities): An instance of the Capabilities class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.capabilities_4b75c5667348309f05b3d70410a39ec1 import Capabilities
        if self._properties.get('Capabilities', None) is not None:
            return self._properties.get('Capabilities')
        else:
            return Capabilities(self)._select()

    @property
    def ControllerTables(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.controllertables_e52142cde8b9a3c55ea6a9f54cffce91.ControllerTables): An instance of the ControllerTables class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.controllertables_e52142cde8b9a3c55ea6a9f54cffce91 import ControllerTables
        if self._properties.get('ControllerTables', None) is not None:
            return self._properties.get('ControllerTables')
        else:
            return ControllerTables(self)

    @property
    def FlowRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowrange_2fd5d93183298b6434d0d9d422fee83c.FlowRange): An instance of the FlowRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowrange_2fd5d93183298b6434d0d9d422fee83c import FlowRange
        if self._properties.get('FlowRange', None) is not None:
            return self._properties.get('FlowRange')
        else:
            return FlowRange(self)

    @property
    def Group(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.group_015e3c040d5ab09e673838caf8d428ba.Group): An instance of the Group class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.group_015e3c040d5ab09e673838caf8d428ba import Group
        if self._properties.get('Group', None) is not None:
            return self._properties.get('Group')
        else:
            return Group(self)

    @property
    def Meter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.meter_780dfd5fbbd89bd8d623eff90a0b890a.Meter): An instance of the Meter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.meter_780dfd5fbbd89bd8d623eff90a0b890a import Meter
        if self._properties.get('Meter', None) is not None:
            return self._properties.get('Meter')
        else:
            return Meter(self)

    @property
    def SupportedActions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.supportedactions_49d9bf4a7b46d52ee0b8746730058977.SupportedActions): An instance of the SupportedActions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.supportedactions_49d9bf4a7b46d52ee0b8746730058977 import SupportedActions
        if self._properties.get('SupportedActions', None) is not None:
            return self._properties.get('SupportedActions')
        else:
            return SupportedActions(self)._select()

    @property
    def SwitchPacketIn(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchpacketin_4f3f94c6a30606d4f42d6b78bc4bcfa2.SwitchPacketIn): An instance of the SwitchPacketIn class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchpacketin_4f3f94c6a30606d4f42d6b78bc4bcfa2 import SwitchPacketIn
        if self._properties.get('SwitchPacketIn', None) is not None:
            return self._properties.get('SwitchPacketIn')
        else:
            return SwitchPacketIn(self)

    @property
    def SwitchPorts(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchports_f5a4eaa4efc61f5b2aadf4ad75b9320e.SwitchPorts): An instance of the SwitchPorts class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchports_f5a4eaa4efc61f5b2aadf4ad75b9320e import SwitchPorts
        if self._properties.get('SwitchPorts', None) is not None:
            return self._properties.get('SwitchPorts')
        else:
            return SwitchPorts(self)

    @property
    def SwitchTables(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchtables_2252edadcb6f8fce8c08ff3edc0bd822.SwitchTables): An instance of the SwitchTables class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchtables_2252edadcb6f8fce8c08ff3edc0bd822 import SwitchTables
        if self._properties.get('SwitchTables', None) is not None:
            return self._properties.get('SwitchTables')
        else:
            return SwitchTables(self)

    @property
    def CalculateFlows(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, calculates the rate at which flows are transmitted by the controller.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CalculateFlows'])
    @CalculateFlows.setter
    def CalculateFlows(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['CalculateFlows'], value)

    @property
    def CalculatePacketInReplyDelay(self):
        # type: () -> bool
        """DEPRECATED 
        Returns
        -------
        - bool: If true, calculates delay between Packet-In sent from Switch and reply received from Controller.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CalculatePacketInReplyDelay'])
    @CalculatePacketInReplyDelay.setter
    def CalculatePacketInReplyDelay(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['CalculatePacketInReplyDelay'], value)

    @property
    def DataPathId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the Datapath ID of the OpenFlow switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathId'])
    @DataPathId.setter
    def DataPathId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['DataPathId'], value)

    @property
    def DataPathIdInHex(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the Datapath ID in hexadecimal format.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DataPathIdInHex'])
    @DataPathIdInHex.setter
    def DataPathIdInHex(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['DataPathIdInHex'], value)

    @property
    def DatapathDescritpion(self):
        # type: () -> str
        """DEPRECATED 
        Returns
        -------
        - str: Indicates a description of the datapath.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DatapathDescritpion'])
    @DatapathDescritpion.setter
    def DatapathDescritpion(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['DatapathDescritpion'], value)

    @property
    def Description(self):
        # type: () -> str
        """
        Returns
        -------
        - str: A description of the OF Channel used to identify it.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Description'])
    @Description.setter
    def Description(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Description'], value)

    @property
    def EnableCalculateFlowsPerSecondUsingBarrierReq(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, enables flow rate Calculation using Barrier request message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableCalculateFlowsPerSecondUsingBarrierReq'])
    @EnableCalculateFlowsPerSecondUsingBarrierReq.setter
    def EnableCalculateFlowsPerSecondUsingBarrierReq(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableCalculateFlowsPerSecondUsingBarrierReq'], value)

    @property
    def EnableHelloElement(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enables Hello element for version negotiation.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableHelloElement'])
    @EnableHelloElement.setter
    def EnableHelloElement(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableHelloElement'], value)

    @property
    def EnableStartupEmptyTableFeatureRequest(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the Table Feature Request is sent at start up. The default value is false
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableStartupEmptyTableFeatureRequest'])
    @EnableStartupEmptyTableFeatureRequest.setter
    def EnableStartupEmptyTableFeatureRequest(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableStartupEmptyTableFeatureRequest'], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, the OF Channel is used in the OpenFlow configuration.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def FlowTxBurstSize(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the number of flows sent in a single burst.
        """
        return self._get_attribute(self._SDM_ATT_MAP['FlowTxBurstSize'])
    @FlowTxBurstSize.setter
    def FlowTxBurstSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['FlowTxBurstSize'], value)

    @property
    def HardwareDescription(self):
        # type: () -> str
        """DEPRECATED 
        Returns
        -------
        - str: Indicates the hardware description of the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['HardwareDescription'])
    @HardwareDescription.setter
    def HardwareDescription(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['HardwareDescription'], value)

    @property
    def InterFlowBurstGap(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the duration, in milliseconds, to wait between successive flow bursts.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterFlowBurstGap'])
    @InterFlowBurstGap.setter
    def InterFlowBurstGap(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['InterFlowBurstGap'], value)

    @property
    def InterPacketInBurstGap(self):
        # type: () -> int
        """DEPRECATED 
        Returns
        -------
        - number: Indicates the duration, in milliseconds, to wait between successive Packet-In bursts.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterPacketInBurstGap'])
    @InterPacketInBurstGap.setter
    def InterPacketInBurstGap(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['InterPacketInBurstGap'], value)

    @property
    def LocalIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the local IP address of the interface. This field is auto-populated and cannot be changed.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LocalIp'])

    @property
    def ManufacturerDescription(self):
        # type: () -> str
        """DEPRECATED 
        Returns
        -------
        - str: Indicates the description of the switch manufacturer.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ManufacturerDescription'])
    @ManufacturerDescription.setter
    def ManufacturerDescription(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['ManufacturerDescription'], value)

    @property
    def MaximumNumberOfFlowsProcessed(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Indicates the maximum number of flows that the controller can advertise before backing off.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaximumNumberOfFlowsProcessed'])
    @MaximumNumberOfFlowsProcessed.setter
    def MaximumNumberOfFlowsProcessed(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['MaximumNumberOfFlowsProcessed'], value)

    @property
    def MaximumPacketInBytes(self):
        # type: () -> int
        """DEPRECATED 
        Returns
        -------
        - number: Indicates the maximum size of data in a Packet-In a message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MaximumPacketInBytes'])
    @MaximumPacketInBytes.setter
    def MaximumPacketInBytes(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['MaximumPacketInBytes'], value)

    @property
    def NumberOfBuffers(self):
        # type: () -> int
        """DEPRECATED 
        Returns
        -------
        - number: Indicates the maximum number of packets that can be stored in the buffered at a time.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfBuffers'])
    @NumberOfBuffers.setter
    def NumberOfBuffers(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['NumberOfBuffers'], value)

    @property
    def PacketInReplyTimeout(self):
        # type: () -> int
        """DEPRECATED 
        Returns
        -------
        - number: Indicates the duration for which the Switch should wait for Packet-in-reply before freeing the buffer.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketInReplyTimeout'])
    @PacketInReplyTimeout.setter
    def PacketInReplyTimeout(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['PacketInReplyTimeout'], value)

    @property
    def PacketInTxBurstSize(self):
        # type: () -> int
        """DEPRECATED 
        Returns
        -------
        - number: Indicates the number of packets in messages sent in a single burst.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PacketInTxBurstSize'])
    @PacketInTxBurstSize.setter
    def PacketInTxBurstSize(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['PacketInTxBurstSize'], value)

    @property
    def RemoteIp(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Indicates the IP address of the DUT at the other end of OF channel.
        """
        return self._get_attribute(self._SDM_ATT_MAP['RemoteIp'])
    @RemoteIp.setter
    def RemoteIp(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['RemoteIp'], value)

    @property
    def SerialNumber(self):
        # type: () -> str
        """DEPRECATED 
        Returns
        -------
        - str: Indicates the Serial Number of the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SerialNumber'])
    @SerialNumber.setter
    def SerialNumber(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['SerialNumber'], value)

    @property
    def SoftwareDescription(self):
        # type: () -> str
        """DEPRECATED 
        Returns
        -------
        - str: Indicates the description of the software installed on the switch.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SoftwareDescription'])
    @SoftwareDescription.setter
    def SoftwareDescription(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['SoftwareDescription'], value)

    @property
    def StartUpGenerationId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: A 64-bit sequence number field that identifies a given mastership view. A new incremented Generation ID is assigned each time the mastership view changes, for instance, when a new master is designated. On receiving a role change request, the switch compares the Generation ID in the message against the largest Generation ID seen so far. A message with a Generation ID smaller than a previously seen Generation ID is discarded.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartUpGenerationId'])
    @StartUpGenerationId.setter
    def StartUpGenerationId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['StartUpGenerationId'], value)

    @property
    def StartUpRoleRequest(self):
        # type: () -> str
        """
        Returns
        -------
        - str(noRoleRequest | master | slave): If selected, the controller sends a Role Request message when connection is established to change its role as per the option selected.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartUpRoleRequest'])
    @StartUpRoleRequest.setter
    def StartUpRoleRequest(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['StartUpRoleRequest'], value)

    @property
    def StartupFeatureRequest(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true, a feature request is sent at startup.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartupFeatureRequest'])
    @StartupFeatureRequest.setter
    def StartupFeatureRequest(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['StartupFeatureRequest'], value)

    @property
    def StoreFlows(self):
        # type: () -> bool
        """DEPRECATED 
        Returns
        -------
        - bool: If true, the switch will store the flows advertised by the controller in its tables.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StoreFlows'])
    @StoreFlows.setter
    def StoreFlows(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['StoreFlows'], value)

    @property
    def UseDataPathIdAsChannelIdentifier(self):
        # type: () -> bool
        """DEPRECATED 
        Returns
        -------
        - bool: If true, the Datapath ID of the switch is used.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseDataPathIdAsChannelIdentifier'])
    @UseDataPathIdAsChannelIdentifier.setter
    def UseDataPathIdAsChannelIdentifier(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['UseDataPathIdAsChannelIdentifier'], value)

    @property
    def UseDatapathId(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Use datapath Id that is configured.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UseDatapathId'])
    @UseDatapathId.setter
    def UseDatapathId(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['UseDatapathId'], value)

    def update(self, CalculateFlows=None, CalculatePacketInReplyDelay=None, DataPathId=None, DataPathIdInHex=None, DatapathDescritpion=None, Description=None, EnableCalculateFlowsPerSecondUsingBarrierReq=None, EnableHelloElement=None, EnableStartupEmptyTableFeatureRequest=None, Enabled=None, FlowTxBurstSize=None, HardwareDescription=None, InterFlowBurstGap=None, InterPacketInBurstGap=None, ManufacturerDescription=None, MaximumNumberOfFlowsProcessed=None, MaximumPacketInBytes=None, NumberOfBuffers=None, PacketInReplyTimeout=None, PacketInTxBurstSize=None, RemoteIp=None, SerialNumber=None, SoftwareDescription=None, StartUpGenerationId=None, StartUpRoleRequest=None, StartupFeatureRequest=None, StoreFlows=None, UseDataPathIdAsChannelIdentifier=None, UseDatapathId=None):
        # type: (bool, bool, str, str, str, str, bool, bool, bool, bool, int, str, int, int, str, int, int, int, int, int, str, str, str, str, str, bool, bool, bool, bool) -> OfChannel
        """Updates ofChannel resource on the server.

        Args
        ----
        - CalculateFlows (bool): If true, calculates the rate at which flows are transmitted by the controller.
        - CalculatePacketInReplyDelay (bool): If true, calculates delay between Packet-In sent from Switch and reply received from Controller.
        - DataPathId (str): Indicates the Datapath ID of the OpenFlow switch.
        - DataPathIdInHex (str): Indicates the Datapath ID in hexadecimal format.
        - DatapathDescritpion (str): Indicates a description of the datapath.
        - Description (str): A description of the OF Channel used to identify it.
        - EnableCalculateFlowsPerSecondUsingBarrierReq (bool): If true, enables flow rate Calculation using Barrier request message.
        - EnableHelloElement (bool): Enables Hello element for version negotiation.
        - EnableStartupEmptyTableFeatureRequest (bool): If true, the Table Feature Request is sent at start up. The default value is false
        - Enabled (bool): If true, the OF Channel is used in the OpenFlow configuration.
        - FlowTxBurstSize (number): Indicates the number of flows sent in a single burst.
        - HardwareDescription (str): Indicates the hardware description of the switch.
        - InterFlowBurstGap (number): Indicates the duration, in milliseconds, to wait between successive flow bursts.
        - InterPacketInBurstGap (number): Indicates the duration, in milliseconds, to wait between successive Packet-In bursts.
        - ManufacturerDescription (str): Indicates the description of the switch manufacturer.
        - MaximumNumberOfFlowsProcessed (number): Indicates the maximum number of flows that the controller can advertise before backing off.
        - MaximumPacketInBytes (number): Indicates the maximum size of data in a Packet-In a message.
        - NumberOfBuffers (number): Indicates the maximum number of packets that can be stored in the buffered at a time.
        - PacketInReplyTimeout (number): Indicates the duration for which the Switch should wait for Packet-in-reply before freeing the buffer.
        - PacketInTxBurstSize (number): Indicates the number of packets in messages sent in a single burst.
        - RemoteIp (str): Indicates the IP address of the DUT at the other end of OF channel.
        - SerialNumber (str): Indicates the Serial Number of the switch.
        - SoftwareDescription (str): Indicates the description of the software installed on the switch.
        - StartUpGenerationId (str): A 64-bit sequence number field that identifies a given mastership view. A new incremented Generation ID is assigned each time the mastership view changes, for instance, when a new master is designated. On receiving a role change request, the switch compares the Generation ID in the message against the largest Generation ID seen so far. A message with a Generation ID smaller than a previously seen Generation ID is discarded.
        - StartUpRoleRequest (str(noRoleRequest | master | slave)): If selected, the controller sends a Role Request message when connection is established to change its role as per the option selected.
        - StartupFeatureRequest (bool): If true, a feature request is sent at startup.
        - StoreFlows (bool): If true, the switch will store the flows advertised by the controller in its tables.
        - UseDataPathIdAsChannelIdentifier (bool): If true, the Datapath ID of the switch is used.
        - UseDatapathId (bool): Use datapath Id that is configured.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, CalculateFlows=None, CalculatePacketInReplyDelay=None, DataPathId=None, DataPathIdInHex=None, DatapathDescritpion=None, Description=None, EnableCalculateFlowsPerSecondUsingBarrierReq=None, EnableHelloElement=None, EnableStartupEmptyTableFeatureRequest=None, Enabled=None, FlowTxBurstSize=None, HardwareDescription=None, InterFlowBurstGap=None, InterPacketInBurstGap=None, ManufacturerDescription=None, MaximumNumberOfFlowsProcessed=None, MaximumPacketInBytes=None, NumberOfBuffers=None, PacketInReplyTimeout=None, PacketInTxBurstSize=None, RemoteIp=None, SerialNumber=None, SoftwareDescription=None, StartUpGenerationId=None, StartUpRoleRequest=None, StartupFeatureRequest=None, StoreFlows=None, UseDataPathIdAsChannelIdentifier=None, UseDatapathId=None):
        # type: (bool, bool, str, str, str, str, bool, bool, bool, bool, int, str, int, int, str, int, int, int, int, int, str, str, str, str, str, bool, bool, bool, bool) -> OfChannel
        """Adds a new ofChannel resource on the server and adds it to the container.

        Args
        ----
        - CalculateFlows (bool): If true, calculates the rate at which flows are transmitted by the controller.
        - CalculatePacketInReplyDelay (bool): If true, calculates delay between Packet-In sent from Switch and reply received from Controller.
        - DataPathId (str): Indicates the Datapath ID of the OpenFlow switch.
        - DataPathIdInHex (str): Indicates the Datapath ID in hexadecimal format.
        - DatapathDescritpion (str): Indicates a description of the datapath.
        - Description (str): A description of the OF Channel used to identify it.
        - EnableCalculateFlowsPerSecondUsingBarrierReq (bool): If true, enables flow rate Calculation using Barrier request message.
        - EnableHelloElement (bool): Enables Hello element for version negotiation.
        - EnableStartupEmptyTableFeatureRequest (bool): If true, the Table Feature Request is sent at start up. The default value is false
        - Enabled (bool): If true, the OF Channel is used in the OpenFlow configuration.
        - FlowTxBurstSize (number): Indicates the number of flows sent in a single burst.
        - HardwareDescription (str): Indicates the hardware description of the switch.
        - InterFlowBurstGap (number): Indicates the duration, in milliseconds, to wait between successive flow bursts.
        - InterPacketInBurstGap (number): Indicates the duration, in milliseconds, to wait between successive Packet-In bursts.
        - ManufacturerDescription (str): Indicates the description of the switch manufacturer.
        - MaximumNumberOfFlowsProcessed (number): Indicates the maximum number of flows that the controller can advertise before backing off.
        - MaximumPacketInBytes (number): Indicates the maximum size of data in a Packet-In a message.
        - NumberOfBuffers (number): Indicates the maximum number of packets that can be stored in the buffered at a time.
        - PacketInReplyTimeout (number): Indicates the duration for which the Switch should wait for Packet-in-reply before freeing the buffer.
        - PacketInTxBurstSize (number): Indicates the number of packets in messages sent in a single burst.
        - RemoteIp (str): Indicates the IP address of the DUT at the other end of OF channel.
        - SerialNumber (str): Indicates the Serial Number of the switch.
        - SoftwareDescription (str): Indicates the description of the software installed on the switch.
        - StartUpGenerationId (str): A 64-bit sequence number field that identifies a given mastership view. A new incremented Generation ID is assigned each time the mastership view changes, for instance, when a new master is designated. On receiving a role change request, the switch compares the Generation ID in the message against the largest Generation ID seen so far. A message with a Generation ID smaller than a previously seen Generation ID is discarded.
        - StartUpRoleRequest (str(noRoleRequest | master | slave)): If selected, the controller sends a Role Request message when connection is established to change its role as per the option selected.
        - StartupFeatureRequest (bool): If true, a feature request is sent at startup.
        - StoreFlows (bool): If true, the switch will store the flows advertised by the controller in its tables.
        - UseDataPathIdAsChannelIdentifier (bool): If true, the Datapath ID of the switch is used.
        - UseDatapathId (bool): Use datapath Id that is configured.

        Returns
        -------
        - self: This instance with all currently retrieved ofChannel resources using find and the newly added ofChannel resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained ofChannel resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, CalculateFlows=None, CalculatePacketInReplyDelay=None, DataPathId=None, DataPathIdInHex=None, DatapathDescritpion=None, Description=None, EnableCalculateFlowsPerSecondUsingBarrierReq=None, EnableHelloElement=None, EnableStartupEmptyTableFeatureRequest=None, Enabled=None, FlowTxBurstSize=None, HardwareDescription=None, InterFlowBurstGap=None, InterPacketInBurstGap=None, LocalIp=None, ManufacturerDescription=None, MaximumNumberOfFlowsProcessed=None, MaximumPacketInBytes=None, NumberOfBuffers=None, PacketInReplyTimeout=None, PacketInTxBurstSize=None, RemoteIp=None, SerialNumber=None, SoftwareDescription=None, StartUpGenerationId=None, StartUpRoleRequest=None, StartupFeatureRequest=None, StoreFlows=None, UseDataPathIdAsChannelIdentifier=None, UseDatapathId=None):
        # type: (bool, bool, str, str, str, str, bool, bool, bool, bool, int, str, int, int, str, str, int, int, int, int, int, str, str, str, str, str, bool, bool, bool, bool) -> OfChannel
        """Finds and retrieves ofChannel resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ofChannel resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ofChannel resources from the server.

        Args
        ----
        - CalculateFlows (bool): If true, calculates the rate at which flows are transmitted by the controller.
        - CalculatePacketInReplyDelay (bool): If true, calculates delay between Packet-In sent from Switch and reply received from Controller.
        - DataPathId (str): Indicates the Datapath ID of the OpenFlow switch.
        - DataPathIdInHex (str): Indicates the Datapath ID in hexadecimal format.
        - DatapathDescritpion (str): Indicates a description of the datapath.
        - Description (str): A description of the OF Channel used to identify it.
        - EnableCalculateFlowsPerSecondUsingBarrierReq (bool): If true, enables flow rate Calculation using Barrier request message.
        - EnableHelloElement (bool): Enables Hello element for version negotiation.
        - EnableStartupEmptyTableFeatureRequest (bool): If true, the Table Feature Request is sent at start up. The default value is false
        - Enabled (bool): If true, the OF Channel is used in the OpenFlow configuration.
        - FlowTxBurstSize (number): Indicates the number of flows sent in a single burst.
        - HardwareDescription (str): Indicates the hardware description of the switch.
        - InterFlowBurstGap (number): Indicates the duration, in milliseconds, to wait between successive flow bursts.
        - InterPacketInBurstGap (number): Indicates the duration, in milliseconds, to wait between successive Packet-In bursts.
        - LocalIp (str): Indicates the local IP address of the interface. This field is auto-populated and cannot be changed.
        - ManufacturerDescription (str): Indicates the description of the switch manufacturer.
        - MaximumNumberOfFlowsProcessed (number): Indicates the maximum number of flows that the controller can advertise before backing off.
        - MaximumPacketInBytes (number): Indicates the maximum size of data in a Packet-In a message.
        - NumberOfBuffers (number): Indicates the maximum number of packets that can be stored in the buffered at a time.
        - PacketInReplyTimeout (number): Indicates the duration for which the Switch should wait for Packet-in-reply before freeing the buffer.
        - PacketInTxBurstSize (number): Indicates the number of packets in messages sent in a single burst.
        - RemoteIp (str): Indicates the IP address of the DUT at the other end of OF channel.
        - SerialNumber (str): Indicates the Serial Number of the switch.
        - SoftwareDescription (str): Indicates the description of the software installed on the switch.
        - StartUpGenerationId (str): A 64-bit sequence number field that identifies a given mastership view. A new incremented Generation ID is assigned each time the mastership view changes, for instance, when a new master is designated. On receiving a role change request, the switch compares the Generation ID in the message against the largest Generation ID seen so far. A message with a Generation ID smaller than a previously seen Generation ID is discarded.
        - StartUpRoleRequest (str(noRoleRequest | master | slave)): If selected, the controller sends a Role Request message when connection is established to change its role as per the option selected.
        - StartupFeatureRequest (bool): If true, a feature request is sent at startup.
        - StoreFlows (bool): If true, the switch will store the flows advertised by the controller in its tables.
        - UseDataPathIdAsChannelIdentifier (bool): If true, the Datapath ID of the switch is used.
        - UseDatapathId (bool): Use datapath Id that is configured.

        Returns
        -------
        - self: This instance with matching ofChannel resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ofChannel data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ofChannel resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def UpdateRole(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[int, None]
        """Executes the updateRole operation on the server.

        NOT DEFINED

        updateRole(async_operation=bool)number
        --------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns number: NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('updateRole', payload=payload, response_object=None)
