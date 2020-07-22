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


class Interface(Base):
    """This object represents a network interface.
    The Interface class encapsulates a list of interface resources that are managed by the user.
    A list of resources can be retrieved from the server using the Interface.find() method.
    The list can be managed by using the Interface.add() and Interface.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'interface'
    _SDM_ATT_MAP = {
        'CircuitAuthType': 'circuitAuthType',
        'CircuitReceivedPasswordList': 'circuitReceivedPasswordList',
        'CircuitTransmitPassword': 'circuitTransmitPassword',
        'ConfiguredHoldTime': 'configuredHoldTime',
        'Enable3WayHandshake': 'enable3WayHandshake',
        'EnableAutoAdjustArea': 'enableAutoAdjustArea',
        'EnableAutoAdjustMtu': 'enableAutoAdjustMtu',
        'EnableAutoAdjustProtocolsSupported': 'enableAutoAdjustProtocolsSupported',
        'EnableBfdRegistration': 'enableBfdRegistration',
        'EnableConfiguredHoldTime': 'enableConfiguredHoldTime',
        'EnableConnectedToDut': 'enableConnectedToDut',
        'Enabled': 'enabled',
        'ExtendedCircuitId': 'extendedCircuitId',
        'InterfaceId': 'interfaceId',
        'InterfaceIp': 'interfaceIp',
        'InterfaceIpMask': 'interfaceIpMask',
        'Ipv6MtMetric': 'ipv6MtMetric',
        'Level': 'level',
        'Level1DeadTime': 'level1DeadTime',
        'Level1HelloTime': 'level1HelloTime',
        'Level2DeadTime': 'level2DeadTime',
        'Level2HelloTime': 'level2HelloTime',
        'Metric': 'metric',
        'NetworkType': 'networkType',
        'PriorityLevel1': 'priorityLevel1',
        'PriorityLevel2': 'priorityLevel2',
        'TeAdminGroup': 'teAdminGroup',
        'TeMaxBandwidth': 'teMaxBandwidth',
        'TeMetricLevel': 'teMetricLevel',
        'TeResMaxBandwidth': 'teResMaxBandwidth',
        'TeUnreservedBwPriority': 'teUnreservedBwPriority',
    }

    def __init__(self, parent):
        super(Interface, self).__init__(parent)

    @property
    def CircuitAuthType(self):
        """
        Returns
        -------
        - str(none | password | md5): The type of Circuit Authentication to be used for this emulated ISIS router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CircuitAuthType'])
    @CircuitAuthType.setter
    def CircuitAuthType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CircuitAuthType'], value)

    @property
    def CircuitReceivedPasswordList(self):
        """
        Returns
        -------
        - list(str): The Receive Password List is used only for Cleartext Password authentication. MD5 Authentication requires that both of the neighbors have the same MD5 key for the packets to be accepted.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CircuitReceivedPasswordList'])
    @CircuitReceivedPasswordList.setter
    def CircuitReceivedPasswordList(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CircuitReceivedPasswordList'], value)

    @property
    def CircuitTransmitPassword(self):
        """
        Returns
        -------
        - str: If circuitAuthType is isisAuthTypePassword, then this is the password (or MD5Key) that will be sent with transmitted IIHs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['CircuitTransmitPassword'])
    @CircuitTransmitPassword.setter
    def CircuitTransmitPassword(self, value):
        self._set_attribute(self._SDM_ATT_MAP['CircuitTransmitPassword'], value)

    @property
    def ConfiguredHoldTime(self):
        """
        Returns
        -------
        - number: The configured hold time for the interface. This value is only used if enableConfiguredHoldTime is set to true.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ConfiguredHoldTime'])
    @ConfiguredHoldTime.setter
    def ConfiguredHoldTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ConfiguredHoldTime'], value)

    @property
    def Enable3WayHandshake(self):
        """
        Returns
        -------
        - bool: If true, Ixia emulated point-to-point circuit will include 3-way TLV in its P2P IIH and attempt to establish the adjacency as specified in RFC 5303.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enable3WayHandshake'])
    @Enable3WayHandshake.setter
    def Enable3WayHandshake(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enable3WayHandshake'], value)

    @property
    def EnableAutoAdjustArea(self):
        """
        Returns
        -------
        - bool: If set, and a HELLO message is received which contains a protocols TLV, then the interfaces protocols will be adjusted to match the received TLV.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAutoAdjustArea'])
    @EnableAutoAdjustArea.setter
    def EnableAutoAdjustArea(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAutoAdjustArea'], value)

    @property
    def EnableAutoAdjustMtu(self):
        """
        Returns
        -------
        - bool: If set, and a padded HELLO message is received on the interface, then the interfaces MTU will be adjusted to match the packet length of the received HELLO message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAutoAdjustMtu'])
    @EnableAutoAdjustMtu.setter
    def EnableAutoAdjustMtu(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAutoAdjustMtu'], value)

    @property
    def EnableAutoAdjustProtocolsSupported(self):
        """
        Returns
        -------
        - bool: If set, and a HELLO message is received which contains a protocols TLV, then the interfaces protocols will be adjusted to match the received TLV.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableAutoAdjustProtocolsSupported'])
    @EnableAutoAdjustProtocolsSupported.setter
    def EnableAutoAdjustProtocolsSupported(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableAutoAdjustProtocolsSupported'], value)

    @property
    def EnableBfdRegistration(self):
        """
        Returns
        -------
        - bool: Indicates if a BFD session is to be created to the ISIS peer IP address once the ISIS session is established. This allows ISIS to use BFD to maintain IPv4 connectivity the ISIS peer.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableBfdRegistration'])
    @EnableBfdRegistration.setter
    def EnableBfdRegistration(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableBfdRegistration'], value)

    @property
    def EnableConfiguredHoldTime(self):
        """
        Returns
        -------
        - bool: If true, enables a hold time for the created interfaces, based on the value set in the configuredHoldTime object.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableConfiguredHoldTime'])
    @EnableConfiguredHoldTime.setter
    def EnableConfiguredHoldTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableConfiguredHoldTime'], value)

    @property
    def EnableConnectedToDut(self):
        """
        Returns
        -------
        - bool: If enabled, this ISIS interface is directly connected to the DUT.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableConnectedToDut'])
    @EnableConnectedToDut.setter
    def EnableConnectedToDut(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableConnectedToDut'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables the use of this interface for the simulated router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def ExtendedCircuitId(self):
        """
        Returns
        -------
        - number: The integer value of the local circuit ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ExtendedCircuitId'])
    @ExtendedCircuitId.setter
    def ExtendedCircuitId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ExtendedCircuitId'], value)

    @property
    def InterfaceId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface): The OSI interface ID for this interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceId'])
    @InterfaceId.setter
    def InterfaceId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceId'], value)

    @property
    def InterfaceIp(self):
        """
        Returns
        -------
        - str: The IP address for this interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceIp'])
    @InterfaceIp.setter
    def InterfaceIp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceIp'], value)

    @property
    def InterfaceIpMask(self):
        """
        Returns
        -------
        - str: Available only when Interface Connected to DUT is disabled. The mask used with the IPv4 address for this virtual interface on the emulated ISIS router. This interface address is used to connect to virtual ISIS Network Ranges behind the Ixia-emulated ISIS router.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceIpMask'])
    @InterfaceIpMask.setter
    def InterfaceIpMask(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceIpMask'], value)

    @property
    def Ipv6MtMetric(self):
        """
        Returns
        -------
        - number: This metric is same as the Interface Metric. If true, it allows you to enter data.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Ipv6MtMetric'])
    @Ipv6MtMetric.setter
    def Ipv6MtMetric(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Ipv6MtMetric'], value)

    @property
    def Level(self):
        """
        Returns
        -------
        - str(level1 | level2 | level1Level2): The IS-IS level associated with the interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Level'])
    @Level.setter
    def Level(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Level'], value)

    @property
    def Level1DeadTime(self):
        """
        Returns
        -------
        - number: The dead (holding time) interval for level 1 hello messages, in seconds. If an ISIS router sending L1 hellos is not heard from within this time period, it will be considered down.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Level1DeadTime'])
    @Level1DeadTime.setter
    def Level1DeadTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Level1DeadTime'], value)

    @property
    def Level1HelloTime(self):
        """
        Returns
        -------
        - number: The hello interval for level 1 hello messages, in seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Level1HelloTime'])
    @Level1HelloTime.setter
    def Level1HelloTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Level1HelloTime'], value)

    @property
    def Level2DeadTime(self):
        """
        Returns
        -------
        - number: The dead (holding time) interval for level 2 hello messages, in seconds. If an ISIS router sending L2 hellos is not heard from within this time period, it will be considered down.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Level2DeadTime'])
    @Level2DeadTime.setter
    def Level2DeadTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Level2DeadTime'], value)

    @property
    def Level2HelloTime(self):
        """
        Returns
        -------
        - number: The hello interval for level 2 hello messages, in seconds.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Level2HelloTime'])
    @Level2HelloTime.setter
    def Level2HelloTime(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Level2HelloTime'], value)

    @property
    def Metric(self):
        """
        Returns
        -------
        - number: The cost metric associated with the route.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Metric'])
    @Metric.setter
    def Metric(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Metric'], value)

    @property
    def NetworkType(self):
        """
        Returns
        -------
        - str(pointToPoint | broadcast | pointToMultipoint): Indicates the type of network attached to the interface: broadcast or point-to-point.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NetworkType'])
    @NetworkType.setter
    def NetworkType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NetworkType'], value)

    @property
    def PriorityLevel1(self):
        """
        Returns
        -------
        - number: Indicates the priority level 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PriorityLevel1'])
    @PriorityLevel1.setter
    def PriorityLevel1(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PriorityLevel1'], value)

    @property
    def PriorityLevel2(self):
        """
        Returns
        -------
        - number: Indicates the priority level 2.
        """
        return self._get_attribute(self._SDM_ATT_MAP['PriorityLevel2'])
    @PriorityLevel2.setter
    def PriorityLevel2(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PriorityLevel2'], value)

    @property
    def TeAdminGroup(self):
        """
        Returns
        -------
        - str: The traffic engineering administrative group associated with the interface. (default = {00 00 00 00})
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeAdminGroup'])
    @TeAdminGroup.setter
    def TeAdminGroup(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeAdminGroup'], value)

    @property
    def TeMaxBandwidth(self):
        """
        Returns
        -------
        - number: For setting the maximum link bandwidth (sub-TLV 9) allowed for this link in this direction. It is a 32-bit IEEE floating point value, in bytes/sec. The default is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeMaxBandwidth'])
    @TeMaxBandwidth.setter
    def TeMaxBandwidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeMaxBandwidth'], value)

    @property
    def TeMetricLevel(self):
        """
        Returns
        -------
        - number: A user-defined metric for this TE path.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeMetricLevel'])
    @TeMetricLevel.setter
    def TeMetricLevel(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeMetricLevel'], value)

    @property
    def TeResMaxBandwidth(self):
        """
        Returns
        -------
        - number: For setting the Maximum reservable link bandwidth (sub-TLV 10). It is the maximum bandwidth that can be reserved for this link in this direction. It is a 32-bit IEEE floating point value, in bytes/sec. The default is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeResMaxBandwidth'])
    @TeResMaxBandwidth.setter
    def TeResMaxBandwidth(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeResMaxBandwidth'], value)

    @property
    def TeUnreservedBwPriority(self):
        """
        Returns
        -------
        - list(number): The traffic engineering unreserved bandwidth for each priority to be advertised. There are eight distinct options. (default = 0.0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['TeUnreservedBwPriority'])
    @TeUnreservedBwPriority.setter
    def TeUnreservedBwPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TeUnreservedBwPriority'], value)

    def update(self, CircuitAuthType=None, CircuitReceivedPasswordList=None, CircuitTransmitPassword=None, ConfiguredHoldTime=None, Enable3WayHandshake=None, EnableAutoAdjustArea=None, EnableAutoAdjustMtu=None, EnableAutoAdjustProtocolsSupported=None, EnableBfdRegistration=None, EnableConfiguredHoldTime=None, EnableConnectedToDut=None, Enabled=None, ExtendedCircuitId=None, InterfaceId=None, InterfaceIp=None, InterfaceIpMask=None, Ipv6MtMetric=None, Level=None, Level1DeadTime=None, Level1HelloTime=None, Level2DeadTime=None, Level2HelloTime=None, Metric=None, NetworkType=None, PriorityLevel1=None, PriorityLevel2=None, TeAdminGroup=None, TeMaxBandwidth=None, TeMetricLevel=None, TeResMaxBandwidth=None, TeUnreservedBwPriority=None):
        """Updates interface resource on the server.

        Args
        ----
        - CircuitAuthType (str(none | password | md5)): The type of Circuit Authentication to be used for this emulated ISIS router.
        - CircuitReceivedPasswordList (list(str)): The Receive Password List is used only for Cleartext Password authentication. MD5 Authentication requires that both of the neighbors have the same MD5 key for the packets to be accepted.
        - CircuitTransmitPassword (str): If circuitAuthType is isisAuthTypePassword, then this is the password (or MD5Key) that will be sent with transmitted IIHs.
        - ConfiguredHoldTime (number): The configured hold time for the interface. This value is only used if enableConfiguredHoldTime is set to true.
        - Enable3WayHandshake (bool): If true, Ixia emulated point-to-point circuit will include 3-way TLV in its P2P IIH and attempt to establish the adjacency as specified in RFC 5303.
        - EnableAutoAdjustArea (bool): If set, and a HELLO message is received which contains a protocols TLV, then the interfaces protocols will be adjusted to match the received TLV.
        - EnableAutoAdjustMtu (bool): If set, and a padded HELLO message is received on the interface, then the interfaces MTU will be adjusted to match the packet length of the received HELLO message.
        - EnableAutoAdjustProtocolsSupported (bool): If set, and a HELLO message is received which contains a protocols TLV, then the interfaces protocols will be adjusted to match the received TLV.
        - EnableBfdRegistration (bool): Indicates if a BFD session is to be created to the ISIS peer IP address once the ISIS session is established. This allows ISIS to use BFD to maintain IPv4 connectivity the ISIS peer.
        - EnableConfiguredHoldTime (bool): If true, enables a hold time for the created interfaces, based on the value set in the configuredHoldTime object.
        - EnableConnectedToDut (bool): If enabled, this ISIS interface is directly connected to the DUT.
        - Enabled (bool): Enables the use of this interface for the simulated router.
        - ExtendedCircuitId (number): The integer value of the local circuit ID.
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): The OSI interface ID for this interface.
        - InterfaceIp (str): The IP address for this interface.
        - InterfaceIpMask (str): Available only when Interface Connected to DUT is disabled. The mask used with the IPv4 address for this virtual interface on the emulated ISIS router. This interface address is used to connect to virtual ISIS Network Ranges behind the Ixia-emulated ISIS router.
        - Ipv6MtMetric (number): This metric is same as the Interface Metric. If true, it allows you to enter data.
        - Level (str(level1 | level2 | level1Level2)): The IS-IS level associated with the interface.
        - Level1DeadTime (number): The dead (holding time) interval for level 1 hello messages, in seconds. If an ISIS router sending L1 hellos is not heard from within this time period, it will be considered down.
        - Level1HelloTime (number): The hello interval for level 1 hello messages, in seconds.
        - Level2DeadTime (number): The dead (holding time) interval for level 2 hello messages, in seconds. If an ISIS router sending L2 hellos is not heard from within this time period, it will be considered down.
        - Level2HelloTime (number): The hello interval for level 2 hello messages, in seconds.
        - Metric (number): The cost metric associated with the route.
        - NetworkType (str(pointToPoint | broadcast | pointToMultipoint)): Indicates the type of network attached to the interface: broadcast or point-to-point.
        - PriorityLevel1 (number): Indicates the priority level 1.
        - PriorityLevel2 (number): Indicates the priority level 2.
        - TeAdminGroup (str): The traffic engineering administrative group associated with the interface. (default = {00 00 00 00})
        - TeMaxBandwidth (number): For setting the maximum link bandwidth (sub-TLV 9) allowed for this link in this direction. It is a 32-bit IEEE floating point value, in bytes/sec. The default is 0.
        - TeMetricLevel (number): A user-defined metric for this TE path.
        - TeResMaxBandwidth (number): For setting the Maximum reservable link bandwidth (sub-TLV 10). It is the maximum bandwidth that can be reserved for this link in this direction. It is a 32-bit IEEE floating point value, in bytes/sec. The default is 0.
        - TeUnreservedBwPriority (list(number)): The traffic engineering unreserved bandwidth for each priority to be advertised. There are eight distinct options. (default = 0.0)

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, CircuitAuthType=None, CircuitReceivedPasswordList=None, CircuitTransmitPassword=None, ConfiguredHoldTime=None, Enable3WayHandshake=None, EnableAutoAdjustArea=None, EnableAutoAdjustMtu=None, EnableAutoAdjustProtocolsSupported=None, EnableBfdRegistration=None, EnableConfiguredHoldTime=None, EnableConnectedToDut=None, Enabled=None, ExtendedCircuitId=None, InterfaceId=None, InterfaceIp=None, InterfaceIpMask=None, Ipv6MtMetric=None, Level=None, Level1DeadTime=None, Level1HelloTime=None, Level2DeadTime=None, Level2HelloTime=None, Metric=None, NetworkType=None, PriorityLevel1=None, PriorityLevel2=None, TeAdminGroup=None, TeMaxBandwidth=None, TeMetricLevel=None, TeResMaxBandwidth=None, TeUnreservedBwPriority=None):
        """Adds a new interface resource on the server and adds it to the container.

        Args
        ----
        - CircuitAuthType (str(none | password | md5)): The type of Circuit Authentication to be used for this emulated ISIS router.
        - CircuitReceivedPasswordList (list(str)): The Receive Password List is used only for Cleartext Password authentication. MD5 Authentication requires that both of the neighbors have the same MD5 key for the packets to be accepted.
        - CircuitTransmitPassword (str): If circuitAuthType is isisAuthTypePassword, then this is the password (or MD5Key) that will be sent with transmitted IIHs.
        - ConfiguredHoldTime (number): The configured hold time for the interface. This value is only used if enableConfiguredHoldTime is set to true.
        - Enable3WayHandshake (bool): If true, Ixia emulated point-to-point circuit will include 3-way TLV in its P2P IIH and attempt to establish the adjacency as specified in RFC 5303.
        - EnableAutoAdjustArea (bool): If set, and a HELLO message is received which contains a protocols TLV, then the interfaces protocols will be adjusted to match the received TLV.
        - EnableAutoAdjustMtu (bool): If set, and a padded HELLO message is received on the interface, then the interfaces MTU will be adjusted to match the packet length of the received HELLO message.
        - EnableAutoAdjustProtocolsSupported (bool): If set, and a HELLO message is received which contains a protocols TLV, then the interfaces protocols will be adjusted to match the received TLV.
        - EnableBfdRegistration (bool): Indicates if a BFD session is to be created to the ISIS peer IP address once the ISIS session is established. This allows ISIS to use BFD to maintain IPv4 connectivity the ISIS peer.
        - EnableConfiguredHoldTime (bool): If true, enables a hold time for the created interfaces, based on the value set in the configuredHoldTime object.
        - EnableConnectedToDut (bool): If enabled, this ISIS interface is directly connected to the DUT.
        - Enabled (bool): Enables the use of this interface for the simulated router.
        - ExtendedCircuitId (number): The integer value of the local circuit ID.
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): The OSI interface ID for this interface.
        - InterfaceIp (str): The IP address for this interface.
        - InterfaceIpMask (str): Available only when Interface Connected to DUT is disabled. The mask used with the IPv4 address for this virtual interface on the emulated ISIS router. This interface address is used to connect to virtual ISIS Network Ranges behind the Ixia-emulated ISIS router.
        - Ipv6MtMetric (number): This metric is same as the Interface Metric. If true, it allows you to enter data.
        - Level (str(level1 | level2 | level1Level2)): The IS-IS level associated with the interface.
        - Level1DeadTime (number): The dead (holding time) interval for level 1 hello messages, in seconds. If an ISIS router sending L1 hellos is not heard from within this time period, it will be considered down.
        - Level1HelloTime (number): The hello interval for level 1 hello messages, in seconds.
        - Level2DeadTime (number): The dead (holding time) interval for level 2 hello messages, in seconds. If an ISIS router sending L2 hellos is not heard from within this time period, it will be considered down.
        - Level2HelloTime (number): The hello interval for level 2 hello messages, in seconds.
        - Metric (number): The cost metric associated with the route.
        - NetworkType (str(pointToPoint | broadcast | pointToMultipoint)): Indicates the type of network attached to the interface: broadcast or point-to-point.
        - PriorityLevel1 (number): Indicates the priority level 1.
        - PriorityLevel2 (number): Indicates the priority level 2.
        - TeAdminGroup (str): The traffic engineering administrative group associated with the interface. (default = {00 00 00 00})
        - TeMaxBandwidth (number): For setting the maximum link bandwidth (sub-TLV 9) allowed for this link in this direction. It is a 32-bit IEEE floating point value, in bytes/sec. The default is 0.
        - TeMetricLevel (number): A user-defined metric for this TE path.
        - TeResMaxBandwidth (number): For setting the Maximum reservable link bandwidth (sub-TLV 10). It is the maximum bandwidth that can be reserved for this link in this direction. It is a 32-bit IEEE floating point value, in bytes/sec. The default is 0.
        - TeUnreservedBwPriority (list(number)): The traffic engineering unreserved bandwidth for each priority to be advertised. There are eight distinct options. (default = 0.0)

        Returns
        -------
        - self: This instance with all currently retrieved interface resources using find and the newly added interface resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained interface resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, CircuitAuthType=None, CircuitReceivedPasswordList=None, CircuitTransmitPassword=None, ConfiguredHoldTime=None, Enable3WayHandshake=None, EnableAutoAdjustArea=None, EnableAutoAdjustMtu=None, EnableAutoAdjustProtocolsSupported=None, EnableBfdRegistration=None, EnableConfiguredHoldTime=None, EnableConnectedToDut=None, Enabled=None, ExtendedCircuitId=None, InterfaceId=None, InterfaceIp=None, InterfaceIpMask=None, Ipv6MtMetric=None, Level=None, Level1DeadTime=None, Level1HelloTime=None, Level2DeadTime=None, Level2HelloTime=None, Metric=None, NetworkType=None, PriorityLevel1=None, PriorityLevel2=None, TeAdminGroup=None, TeMaxBandwidth=None, TeMetricLevel=None, TeResMaxBandwidth=None, TeUnreservedBwPriority=None):
        """Finds and retrieves interface resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve interface resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all interface resources from the server.

        Args
        ----
        - CircuitAuthType (str(none | password | md5)): The type of Circuit Authentication to be used for this emulated ISIS router.
        - CircuitReceivedPasswordList (list(str)): The Receive Password List is used only for Cleartext Password authentication. MD5 Authentication requires that both of the neighbors have the same MD5 key for the packets to be accepted.
        - CircuitTransmitPassword (str): If circuitAuthType is isisAuthTypePassword, then this is the password (or MD5Key) that will be sent with transmitted IIHs.
        - ConfiguredHoldTime (number): The configured hold time for the interface. This value is only used if enableConfiguredHoldTime is set to true.
        - Enable3WayHandshake (bool): If true, Ixia emulated point-to-point circuit will include 3-way TLV in its P2P IIH and attempt to establish the adjacency as specified in RFC 5303.
        - EnableAutoAdjustArea (bool): If set, and a HELLO message is received which contains a protocols TLV, then the interfaces protocols will be adjusted to match the received TLV.
        - EnableAutoAdjustMtu (bool): If set, and a padded HELLO message is received on the interface, then the interfaces MTU will be adjusted to match the packet length of the received HELLO message.
        - EnableAutoAdjustProtocolsSupported (bool): If set, and a HELLO message is received which contains a protocols TLV, then the interfaces protocols will be adjusted to match the received TLV.
        - EnableBfdRegistration (bool): Indicates if a BFD session is to be created to the ISIS peer IP address once the ISIS session is established. This allows ISIS to use BFD to maintain IPv4 connectivity the ISIS peer.
        - EnableConfiguredHoldTime (bool): If true, enables a hold time for the created interfaces, based on the value set in the configuredHoldTime object.
        - EnableConnectedToDut (bool): If enabled, this ISIS interface is directly connected to the DUT.
        - Enabled (bool): Enables the use of this interface for the simulated router.
        - ExtendedCircuitId (number): The integer value of the local circuit ID.
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): The OSI interface ID for this interface.
        - InterfaceIp (str): The IP address for this interface.
        - InterfaceIpMask (str): Available only when Interface Connected to DUT is disabled. The mask used with the IPv4 address for this virtual interface on the emulated ISIS router. This interface address is used to connect to virtual ISIS Network Ranges behind the Ixia-emulated ISIS router.
        - Ipv6MtMetric (number): This metric is same as the Interface Metric. If true, it allows you to enter data.
        - Level (str(level1 | level2 | level1Level2)): The IS-IS level associated with the interface.
        - Level1DeadTime (number): The dead (holding time) interval for level 1 hello messages, in seconds. If an ISIS router sending L1 hellos is not heard from within this time period, it will be considered down.
        - Level1HelloTime (number): The hello interval for level 1 hello messages, in seconds.
        - Level2DeadTime (number): The dead (holding time) interval for level 2 hello messages, in seconds. If an ISIS router sending L2 hellos is not heard from within this time period, it will be considered down.
        - Level2HelloTime (number): The hello interval for level 2 hello messages, in seconds.
        - Metric (number): The cost metric associated with the route.
        - NetworkType (str(pointToPoint | broadcast | pointToMultipoint)): Indicates the type of network attached to the interface: broadcast or point-to-point.
        - PriorityLevel1 (number): Indicates the priority level 1.
        - PriorityLevel2 (number): Indicates the priority level 2.
        - TeAdminGroup (str): The traffic engineering administrative group associated with the interface. (default = {00 00 00 00})
        - TeMaxBandwidth (number): For setting the maximum link bandwidth (sub-TLV 9) allowed for this link in this direction. It is a 32-bit IEEE floating point value, in bytes/sec. The default is 0.
        - TeMetricLevel (number): A user-defined metric for this TE path.
        - TeResMaxBandwidth (number): For setting the Maximum reservable link bandwidth (sub-TLV 10). It is the maximum bandwidth that can be reserved for this link in this direction. It is a 32-bit IEEE floating point value, in bytes/sec. The default is 0.
        - TeUnreservedBwPriority (list(number)): The traffic engineering unreserved bandwidth for each priority to be advertised. There are eight distinct options. (default = 0.0)

        Returns
        -------
        - self: This instance with matching interface resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of interface data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the interface resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
