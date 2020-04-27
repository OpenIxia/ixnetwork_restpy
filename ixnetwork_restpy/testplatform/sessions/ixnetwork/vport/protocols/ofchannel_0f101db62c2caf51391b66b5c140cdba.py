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


class OfChannel(Base):
    """Signifies the OF Channel used in this protocol configuration.
    The OfChannel class encapsulates a list of ofChannel resources that are managed by the user.
    A list of resources can be retrieved from the server using the OfChannel.find() method.
    The list can be managed by using the OfChannel.add() and OfChannel.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ofChannel'

    def __init__(self, parent):
        super(OfChannel, self).__init__(parent)

    @property
    def Capabilities(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.capabilities_1a0619d7508f1d1f20abc05725d1c184.Capabilities): An instance of the Capabilities class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.capabilities_1a0619d7508f1d1f20abc05725d1c184 import Capabilities
        return Capabilities(self)._select()

    @property
    def ControllerTables(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.controllertables_52158f37bd446e1485e6aede1509717b.ControllerTables): An instance of the ControllerTables class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.controllertables_52158f37bd446e1485e6aede1509717b import ControllerTables
        return ControllerTables(self)

    @property
    def FlowRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowrange_798e340f4a4995ed80ccf60bc89a0cda.FlowRange): An instance of the FlowRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.flowrange_798e340f4a4995ed80ccf60bc89a0cda import FlowRange
        return FlowRange(self)

    @property
    def Group(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.group_35180f1dc6dec0522d6ddc3fa3ea80f2.Group): An instance of the Group class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.group_35180f1dc6dec0522d6ddc3fa3ea80f2 import Group
        return Group(self)

    @property
    def Meter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.meter_da68b7c16796411cc3f527552467fbba.Meter): An instance of the Meter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.meter_da68b7c16796411cc3f527552467fbba import Meter
        return Meter(self)

    @property
    def SupportedActions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.supportedactions_c4844246a6355ace90b8ed0877bb2b06.SupportedActions): An instance of the SupportedActions class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.supportedactions_c4844246a6355ace90b8ed0877bb2b06 import SupportedActions
        return SupportedActions(self)._select()

    @property
    def SwitchPacketIn(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchpacketin_1a9a9aab92b2a211158ff03d5f1e6e00.SwitchPacketIn): An instance of the SwitchPacketIn class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchpacketin_1a9a9aab92b2a211158ff03d5f1e6e00 import SwitchPacketIn
        return SwitchPacketIn(self)

    @property
    def SwitchPorts(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchports_56d807b61677f8ba5c05603f473b858d.SwitchPorts): An instance of the SwitchPorts class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchports_56d807b61677f8ba5c05603f473b858d import SwitchPorts
        return SwitchPorts(self)

    @property
    def SwitchTables(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchtables_3a0a5bfd815ff10901882ee34a34fb0b.SwitchTables): An instance of the SwitchTables class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.switchtables_3a0a5bfd815ff10901882ee34a34fb0b import SwitchTables
        return SwitchTables(self)

    @property
    def CalculateFlows(self):
        """
        Returns
        -------
        - bool: If true, calculates the rate at which flows are transmitted by the controller.
        """
        return self._get_attribute('calculateFlows')
    @CalculateFlows.setter
    def CalculateFlows(self, value):
        self._set_attribute('calculateFlows', value)

    @property
    def CalculatePacketInReplyDelay(self):
        """DEPRECATED 
        Returns
        -------
        - bool: If true, calculates delay between Packet-In sent from Switch and reply received from Controller.
        """
        return self._get_attribute('calculatePacketInReplyDelay')
    @CalculatePacketInReplyDelay.setter
    def CalculatePacketInReplyDelay(self, value):
        self._set_attribute('calculatePacketInReplyDelay', value)

    @property
    def DataPathId(self):
        """
        Returns
        -------
        - str: Indicates the Datapath ID of the OpenFlow switch.
        """
        return self._get_attribute('dataPathId')
    @DataPathId.setter
    def DataPathId(self, value):
        self._set_attribute('dataPathId', value)

    @property
    def DataPathIdInHex(self):
        """
        Returns
        -------
        - str: Indicates the Datapath ID in hexadecimal format.
        """
        return self._get_attribute('dataPathIdInHex')
    @DataPathIdInHex.setter
    def DataPathIdInHex(self, value):
        self._set_attribute('dataPathIdInHex', value)

    @property
    def DatapathDescritpion(self):
        """DEPRECATED 
        Returns
        -------
        - str: Indicates a description of the datapath.
        """
        return self._get_attribute('datapathDescritpion')
    @DatapathDescritpion.setter
    def DatapathDescritpion(self, value):
        self._set_attribute('datapathDescritpion', value)

    @property
    def Description(self):
        """
        Returns
        -------
        - str: A description of the OF Channel used to identify it.
        """
        return self._get_attribute('description')
    @Description.setter
    def Description(self, value):
        self._set_attribute('description', value)

    @property
    def EnableCalculateFlowsPerSecondUsingBarrierReq(self):
        """
        Returns
        -------
        - bool: If true, enables flow rate Calculation using Barrier request message.
        """
        return self._get_attribute('enableCalculateFlowsPerSecondUsingBarrierReq')
    @EnableCalculateFlowsPerSecondUsingBarrierReq.setter
    def EnableCalculateFlowsPerSecondUsingBarrierReq(self, value):
        self._set_attribute('enableCalculateFlowsPerSecondUsingBarrierReq', value)

    @property
    def EnableHelloElement(self):
        """
        Returns
        -------
        - bool: Enables Hello element for version negotiation.
        """
        return self._get_attribute('enableHelloElement')
    @EnableHelloElement.setter
    def EnableHelloElement(self, value):
        self._set_attribute('enableHelloElement', value)

    @property
    def EnableStartupEmptyTableFeatureRequest(self):
        """
        Returns
        -------
        - bool: If true, the Table Feature Request is sent at start up. The default value is false
        """
        return self._get_attribute('enableStartupEmptyTableFeatureRequest')
    @EnableStartupEmptyTableFeatureRequest.setter
    def EnableStartupEmptyTableFeatureRequest(self, value):
        self._set_attribute('enableStartupEmptyTableFeatureRequest', value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, the OF Channel is used in the OpenFlow configuration.
        """
        return self._get_attribute('enabled')
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute('enabled', value)

    @property
    def FlowTxBurstSize(self):
        """
        Returns
        -------
        - number: Indicates the number of flows sent in a single burst.
        """
        return self._get_attribute('flowTxBurstSize')
    @FlowTxBurstSize.setter
    def FlowTxBurstSize(self, value):
        self._set_attribute('flowTxBurstSize', value)

    @property
    def HardwareDescription(self):
        """DEPRECATED 
        Returns
        -------
        - str: Indicates the hardware description of the switch.
        """
        return self._get_attribute('hardwareDescription')
    @HardwareDescription.setter
    def HardwareDescription(self, value):
        self._set_attribute('hardwareDescription', value)

    @property
    def InterFlowBurstGap(self):
        """
        Returns
        -------
        - number: Indicates the duration, in milliseconds, to wait between successive flow bursts.
        """
        return self._get_attribute('interFlowBurstGap')
    @InterFlowBurstGap.setter
    def InterFlowBurstGap(self, value):
        self._set_attribute('interFlowBurstGap', value)

    @property
    def InterPacketInBurstGap(self):
        """DEPRECATED 
        Returns
        -------
        - number: Indicates the duration, in milliseconds, to wait between successive Packet-In bursts.
        """
        return self._get_attribute('interPacketInBurstGap')
    @InterPacketInBurstGap.setter
    def InterPacketInBurstGap(self, value):
        self._set_attribute('interPacketInBurstGap', value)

    @property
    def LocalIp(self):
        """
        Returns
        -------
        - str: Indicates the local IP address of the interface. This field is auto-populated and cannot be changed.
        """
        return self._get_attribute('localIp')

    @property
    def ManufacturerDescription(self):
        """DEPRECATED 
        Returns
        -------
        - str: Indicates the description of the switch manufacturer.
        """
        return self._get_attribute('manufacturerDescription')
    @ManufacturerDescription.setter
    def ManufacturerDescription(self, value):
        self._set_attribute('manufacturerDescription', value)

    @property
    def MaximumNumberOfFlowsProcessed(self):
        """
        Returns
        -------
        - number: Indicates the maximum number of flows that the controller can advertise before backing off.
        """
        return self._get_attribute('maximumNumberOfFlowsProcessed')
    @MaximumNumberOfFlowsProcessed.setter
    def MaximumNumberOfFlowsProcessed(self, value):
        self._set_attribute('maximumNumberOfFlowsProcessed', value)

    @property
    def MaximumPacketInBytes(self):
        """DEPRECATED 
        Returns
        -------
        - number: Indicates the maximum size of data in a Packet-In a message.
        """
        return self._get_attribute('maximumPacketInBytes')
    @MaximumPacketInBytes.setter
    def MaximumPacketInBytes(self, value):
        self._set_attribute('maximumPacketInBytes', value)

    @property
    def NumberOfBuffers(self):
        """DEPRECATED 
        Returns
        -------
        - number: Indicates the maximum number of packets that can be stored in the buffered at a time.
        """
        return self._get_attribute('numberOfBuffers')
    @NumberOfBuffers.setter
    def NumberOfBuffers(self, value):
        self._set_attribute('numberOfBuffers', value)

    @property
    def PacketInReplyTimeout(self):
        """DEPRECATED 
        Returns
        -------
        - number: Indicates the duration for which the Switch should wait for Packet-in-reply before freeing the buffer.
        """
        return self._get_attribute('packetInReplyTimeout')
    @PacketInReplyTimeout.setter
    def PacketInReplyTimeout(self, value):
        self._set_attribute('packetInReplyTimeout', value)

    @property
    def PacketInTxBurstSize(self):
        """DEPRECATED 
        Returns
        -------
        - number: Indicates the number of packets in messages sent in a single burst.
        """
        return self._get_attribute('packetInTxBurstSize')
    @PacketInTxBurstSize.setter
    def PacketInTxBurstSize(self, value):
        self._set_attribute('packetInTxBurstSize', value)

    @property
    def RemoteIp(self):
        """
        Returns
        -------
        - str: Indicates the IP address of the DUT at the other end of OF channel.
        """
        return self._get_attribute('remoteIp')
    @RemoteIp.setter
    def RemoteIp(self, value):
        self._set_attribute('remoteIp', value)

    @property
    def SerialNumber(self):
        """DEPRECATED 
        Returns
        -------
        - str: Indicates the Serial Number of the switch.
        """
        return self._get_attribute('serialNumber')
    @SerialNumber.setter
    def SerialNumber(self, value):
        self._set_attribute('serialNumber', value)

    @property
    def SoftwareDescription(self):
        """DEPRECATED 
        Returns
        -------
        - str: Indicates the description of the software installed on the switch.
        """
        return self._get_attribute('softwareDescription')
    @SoftwareDescription.setter
    def SoftwareDescription(self, value):
        self._set_attribute('softwareDescription', value)

    @property
    def StartUpGenerationId(self):
        """
        Returns
        -------
        - str: A 64-bit sequence number field that identifies a given mastership view. A new incremented Generation ID is assigned each time the mastership view changes, for instance, when a new master is designated. On receiving a role change request, the switch compares the Generation ID in the message against the largest Generation ID seen so far. A message with a Generation ID smaller than a previously seen Generation ID is discarded.
        """
        return self._get_attribute('startUpGenerationId')
    @StartUpGenerationId.setter
    def StartUpGenerationId(self, value):
        self._set_attribute('startUpGenerationId', value)

    @property
    def StartUpRoleRequest(self):
        """
        Returns
        -------
        - str(noRoleRequest | master | slave): If selected, the controller sends a Role Request message when connection is established to change its role as per the option selected.
        """
        return self._get_attribute('startUpRoleRequest')
    @StartUpRoleRequest.setter
    def StartUpRoleRequest(self, value):
        self._set_attribute('startUpRoleRequest', value)

    @property
    def StartupFeatureRequest(self):
        """
        Returns
        -------
        - bool: If true, a feature request is sent at startup.
        """
        return self._get_attribute('startupFeatureRequest')
    @StartupFeatureRequest.setter
    def StartupFeatureRequest(self, value):
        self._set_attribute('startupFeatureRequest', value)

    @property
    def StoreFlows(self):
        """DEPRECATED 
        Returns
        -------
        - bool: If true, the switch will store the flows advertised by the controller in its tables.
        """
        return self._get_attribute('storeFlows')
    @StoreFlows.setter
    def StoreFlows(self, value):
        self._set_attribute('storeFlows', value)

    @property
    def UseDataPathIdAsChannelIdentifier(self):
        """DEPRECATED 
        Returns
        -------
        - bool: If true, the Datapath ID of the switch is used.
        """
        return self._get_attribute('useDataPathIdAsChannelIdentifier')
    @UseDataPathIdAsChannelIdentifier.setter
    def UseDataPathIdAsChannelIdentifier(self, value):
        self._set_attribute('useDataPathIdAsChannelIdentifier', value)

    @property
    def UseDatapathId(self):
        """
        Returns
        -------
        - bool: Use datapath Id that is configured.
        """
        return self._get_attribute('useDatapathId')
    @UseDatapathId.setter
    def UseDatapathId(self, value):
        self._set_attribute('useDatapathId', value)

    def update(self, CalculateFlows=None, CalculatePacketInReplyDelay=None, DataPathId=None, DataPathIdInHex=None, DatapathDescritpion=None, Description=None, EnableCalculateFlowsPerSecondUsingBarrierReq=None, EnableHelloElement=None, EnableStartupEmptyTableFeatureRequest=None, Enabled=None, FlowTxBurstSize=None, HardwareDescription=None, InterFlowBurstGap=None, InterPacketInBurstGap=None, ManufacturerDescription=None, MaximumNumberOfFlowsProcessed=None, MaximumPacketInBytes=None, NumberOfBuffers=None, PacketInReplyTimeout=None, PacketInTxBurstSize=None, RemoteIp=None, SerialNumber=None, SoftwareDescription=None, StartUpGenerationId=None, StartUpRoleRequest=None, StartupFeatureRequest=None, StoreFlows=None, UseDataPathIdAsChannelIdentifier=None, UseDatapathId=None):
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
        return self._update(locals())

    def add(self, CalculateFlows=None, CalculatePacketInReplyDelay=None, DataPathId=None, DataPathIdInHex=None, DatapathDescritpion=None, Description=None, EnableCalculateFlowsPerSecondUsingBarrierReq=None, EnableHelloElement=None, EnableStartupEmptyTableFeatureRequest=None, Enabled=None, FlowTxBurstSize=None, HardwareDescription=None, InterFlowBurstGap=None, InterPacketInBurstGap=None, ManufacturerDescription=None, MaximumNumberOfFlowsProcessed=None, MaximumPacketInBytes=None, NumberOfBuffers=None, PacketInReplyTimeout=None, PacketInTxBurstSize=None, RemoteIp=None, SerialNumber=None, SoftwareDescription=None, StartUpGenerationId=None, StartUpRoleRequest=None, StartupFeatureRequest=None, StoreFlows=None, UseDataPathIdAsChannelIdentifier=None, UseDatapathId=None):
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
        return self._create(locals())

    def remove(self):
        """Deletes all the contained ofChannel resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, CalculateFlows=None, CalculatePacketInReplyDelay=None, DataPathId=None, DataPathIdInHex=None, DatapathDescritpion=None, Description=None, EnableCalculateFlowsPerSecondUsingBarrierReq=None, EnableHelloElement=None, EnableStartupEmptyTableFeatureRequest=None, Enabled=None, FlowTxBurstSize=None, HardwareDescription=None, InterFlowBurstGap=None, InterPacketInBurstGap=None, LocalIp=None, ManufacturerDescription=None, MaximumNumberOfFlowsProcessed=None, MaximumPacketInBytes=None, NumberOfBuffers=None, PacketInReplyTimeout=None, PacketInTxBurstSize=None, RemoteIp=None, SerialNumber=None, SoftwareDescription=None, StartUpGenerationId=None, StartUpRoleRequest=None, StartupFeatureRequest=None, StoreFlows=None, UseDataPathIdAsChannelIdentifier=None, UseDatapathId=None):
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
        return self._select(locals())

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

    def UpdateRole(self):
        """Executes the updateRole operation on the server.

        NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('updateRole', payload=payload, response_object=None)
