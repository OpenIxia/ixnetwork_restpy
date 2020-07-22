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


class Host(Base):
    """A list of simulated hosts which received multicast traffic.
    The Host class encapsulates a list of host resources that are managed by the user.
    A list of resources can be retrieved from the server using the Host.find() method.
    The list can be managed by using the Host.add() and Host.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'host'
    _SDM_ATT_MAP = {
        'EnableImmediateResp': 'enableImmediateResp',
        'EnableQueryResMode': 'enableQueryResMode',
        'EnableRouterAlert': 'enableRouterAlert',
        'EnableSpecificResMode': 'enableSpecificResMode',
        'EnableSuppressReport': 'enableSuppressReport',
        'EnableUnsolicitedResMode': 'enableUnsolicitedResMode',
        'Enabled': 'enabled',
        'InterfaceIndex': 'interfaceIndex',
        'InterfaceType': 'interfaceType',
        'Interfaces': 'interfaces',
        'ProtocolInterface': 'protocolInterface',
        'ReportFreq': 'reportFreq',
        'RobustnessVariable': 'robustnessVariable',
        'TrafficGroupId': 'trafficGroupId',
        'Version': 'version',
    }

    def __init__(self, parent):
        super(Host, self).__init__(parent)

    @property
    def GroupRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.grouprange_24a71c3cd8132c5bc9c3c0de300abf10.GroupRange): An instance of the GroupRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.grouprange_24a71c3cd8132c5bc9c3c0de300abf10 import GroupRange
        return GroupRange(self)

    @property
    def EnableImmediateResp(self):
        """
        Returns
        -------
        - bool: If enabled, the MLD host will ignore the value specified in the maximum response delay in the query message, assume that the delay is always = 0 seconds, and immediately respond to the query by sending a report.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableImmediateResp'])
    @EnableImmediateResp.setter
    def EnableImmediateResp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableImmediateResp'], value)

    @property
    def EnableQueryResMode(self):
        """
        Returns
        -------
        - bool: Enables the simulation for the host to respond to general queries.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableQueryResMode'])
    @EnableQueryResMode.setter
    def EnableQueryResMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableQueryResMode'], value)

    @property
    def EnableRouterAlert(self):
        """
        Returns
        -------
        - bool: Sets the router alert bit in listener report messages.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableRouterAlert'])
    @EnableRouterAlert.setter
    def EnableRouterAlert(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableRouterAlert'], value)

    @property
    def EnableSpecificResMode(self):
        """
        Returns
        -------
        - bool: Enables the simulation for the host to respond to group specific queries.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSpecificResMode'])
    @EnableSpecificResMode.setter
    def EnableSpecificResMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSpecificResMode'], value)

    @property
    def EnableSuppressReport(self):
        """
        Returns
        -------
        - bool: Suppress generation of V2 reports on receipt of v1 reports having common groups. If enabled, it indicates that a host/group member will allow its MLDv2 Membership Record to be 'suppressed by a membership report for Version 1. The suppression will only be for group reports received from another port.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSuppressReport'])
    @EnableSuppressReport.setter
    def EnableSuppressReport(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSuppressReport'], value)

    @property
    def EnableUnsolicitedResMode(self):
        """
        Returns
        -------
        - bool: If enabled, causes the emulated MLD host to automatically send full membership messages at regular intervals, without waiting for a query message.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableUnsolicitedResMode'])
    @EnableUnsolicitedResMode.setter
    def EnableUnsolicitedResMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableUnsolicitedResMode'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables the use of the host in the MLD simulation.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def InterfaceIndex(self):
        """
        Returns
        -------
        - number: The assigned protocol interface ID for this MLD interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceIndex'])
    @InterfaceIndex.setter
    def InterfaceIndex(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceIndex'], value)

    @property
    def InterfaceType(self):
        """
        Returns
        -------
        - str: The type of interface to be selected for this MLD interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceType'])
    @InterfaceType.setter
    def InterfaceType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceType'], value)

    @property
    def Interfaces(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range): The interfaces that are associated with the selected interface type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Interfaces'])
    @Interfaces.setter
    def Interfaces(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Interfaces'], value)

    @property
    def ProtocolInterface(self):
        """DEPRECATED 
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface): The name of the protocol interface being used for this emulated MLD Host. There may be multiple IPv6 protocol interfaces to select from.NOTE: Only enabled protocol interfaces configured with IPv6 addresses will be listed here.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ProtocolInterface'])
    @ProtocolInterface.setter
    def ProtocolInterface(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ProtocolInterface'], value)

    @property
    def ReportFreq(self):
        """
        Returns
        -------
        - number: Can be configured only when the Unsolicited Response Mode option is enabled. Otherwise, it is read-only. When Unsolicited Response Mode is enabled, specifies the frequency, in seconds, with which unsolicited messages are generated.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ReportFreq'])
    @ReportFreq.setter
    def ReportFreq(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ReportFreq'], value)

    @property
    def RobustnessVariable(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['RobustnessVariable'])
    @RobustnessVariable.setter
    def RobustnessVariable(self, value):
        self._set_attribute(self._SDM_ATT_MAP['RobustnessVariable'], value)

    @property
    def TrafficGroupId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficGroupId'])
    @TrafficGroupId.setter
    def TrafficGroupId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficGroupId'], value)

    @property
    def Version(self):
        """
        Returns
        -------
        - str(version1 | version2): Sets the MLD version number that is to be simulated on the host: 1 or 2.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Version'])
    @Version.setter
    def Version(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Version'], value)

    def update(self, EnableImmediateResp=None, EnableQueryResMode=None, EnableRouterAlert=None, EnableSpecificResMode=None, EnableSuppressReport=None, EnableUnsolicitedResMode=None, Enabled=None, InterfaceIndex=None, InterfaceType=None, Interfaces=None, ProtocolInterface=None, ReportFreq=None, RobustnessVariable=None, TrafficGroupId=None, Version=None):
        """Updates host resource on the server.

        Args
        ----
        - EnableImmediateResp (bool): If enabled, the MLD host will ignore the value specified in the maximum response delay in the query message, assume that the delay is always = 0 seconds, and immediately respond to the query by sending a report.
        - EnableQueryResMode (bool): Enables the simulation for the host to respond to general queries.
        - EnableRouterAlert (bool): Sets the router alert bit in listener report messages.
        - EnableSpecificResMode (bool): Enables the simulation for the host to respond to group specific queries.
        - EnableSuppressReport (bool): Suppress generation of V2 reports on receipt of v1 reports having common groups. If enabled, it indicates that a host/group member will allow its MLDv2 Membership Record to be 'suppressed by a membership report for Version 1. The suppression will only be for group reports received from another port.
        - EnableUnsolicitedResMode (bool): If enabled, causes the emulated MLD host to automatically send full membership messages at regular intervals, without waiting for a query message.
        - Enabled (bool): Enables the use of the host in the MLD simulation.
        - InterfaceIndex (number): The assigned protocol interface ID for this MLD interface.
        - InterfaceType (str): The type of interface to be selected for this MLD interface.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range)): The interfaces that are associated with the selected interface type.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): The name of the protocol interface being used for this emulated MLD Host. There may be multiple IPv6 protocol interfaces to select from.NOTE: Only enabled protocol interfaces configured with IPv6 addresses will be listed here.
        - ReportFreq (number): Can be configured only when the Unsolicited Response Mode option is enabled. Otherwise, it is read-only. When Unsolicited Response Mode is enabled, specifies the frequency, in seconds, with which unsolicited messages are generated.
        - RobustnessVariable (number): NOT DEFINED
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        - Version (str(version1 | version2)): Sets the MLD version number that is to be simulated on the host: 1 or 2.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, EnableImmediateResp=None, EnableQueryResMode=None, EnableRouterAlert=None, EnableSpecificResMode=None, EnableSuppressReport=None, EnableUnsolicitedResMode=None, Enabled=None, InterfaceIndex=None, InterfaceType=None, Interfaces=None, ProtocolInterface=None, ReportFreq=None, RobustnessVariable=None, TrafficGroupId=None, Version=None):
        """Adds a new host resource on the server and adds it to the container.

        Args
        ----
        - EnableImmediateResp (bool): If enabled, the MLD host will ignore the value specified in the maximum response delay in the query message, assume that the delay is always = 0 seconds, and immediately respond to the query by sending a report.
        - EnableQueryResMode (bool): Enables the simulation for the host to respond to general queries.
        - EnableRouterAlert (bool): Sets the router alert bit in listener report messages.
        - EnableSpecificResMode (bool): Enables the simulation for the host to respond to group specific queries.
        - EnableSuppressReport (bool): Suppress generation of V2 reports on receipt of v1 reports having common groups. If enabled, it indicates that a host/group member will allow its MLDv2 Membership Record to be 'suppressed by a membership report for Version 1. The suppression will only be for group reports received from another port.
        - EnableUnsolicitedResMode (bool): If enabled, causes the emulated MLD host to automatically send full membership messages at regular intervals, without waiting for a query message.
        - Enabled (bool): Enables the use of the host in the MLD simulation.
        - InterfaceIndex (number): The assigned protocol interface ID for this MLD interface.
        - InterfaceType (str): The type of interface to be selected for this MLD interface.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range)): The interfaces that are associated with the selected interface type.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): The name of the protocol interface being used for this emulated MLD Host. There may be multiple IPv6 protocol interfaces to select from.NOTE: Only enabled protocol interfaces configured with IPv6 addresses will be listed here.
        - ReportFreq (number): Can be configured only when the Unsolicited Response Mode option is enabled. Otherwise, it is read-only. When Unsolicited Response Mode is enabled, specifies the frequency, in seconds, with which unsolicited messages are generated.
        - RobustnessVariable (number): NOT DEFINED
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        - Version (str(version1 | version2)): Sets the MLD version number that is to be simulated on the host: 1 or 2.

        Returns
        -------
        - self: This instance with all currently retrieved host resources using find and the newly added host resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained host resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, EnableImmediateResp=None, EnableQueryResMode=None, EnableRouterAlert=None, EnableSpecificResMode=None, EnableSuppressReport=None, EnableUnsolicitedResMode=None, Enabled=None, InterfaceIndex=None, InterfaceType=None, Interfaces=None, ProtocolInterface=None, ReportFreq=None, RobustnessVariable=None, TrafficGroupId=None, Version=None):
        """Finds and retrieves host resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve host resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all host resources from the server.

        Args
        ----
        - EnableImmediateResp (bool): If enabled, the MLD host will ignore the value specified in the maximum response delay in the query message, assume that the delay is always = 0 seconds, and immediately respond to the query by sending a report.
        - EnableQueryResMode (bool): Enables the simulation for the host to respond to general queries.
        - EnableRouterAlert (bool): Sets the router alert bit in listener report messages.
        - EnableSpecificResMode (bool): Enables the simulation for the host to respond to group specific queries.
        - EnableSuppressReport (bool): Suppress generation of V2 reports on receipt of v1 reports having common groups. If enabled, it indicates that a host/group member will allow its MLDv2 Membership Record to be 'suppressed by a membership report for Version 1. The suppression will only be for group reports received from another port.
        - EnableUnsolicitedResMode (bool): If enabled, causes the emulated MLD host to automatically send full membership messages at regular intervals, without waiting for a query message.
        - Enabled (bool): Enables the use of the host in the MLD simulation.
        - InterfaceIndex (number): The assigned protocol interface ID for this MLD interface.
        - InterfaceType (str): The type of interface to be selected for this MLD interface.
        - Interfaces (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range | /api/v1/sessions/1/ixnetwork/vport/.../range)): The interfaces that are associated with the selected interface type.
        - ProtocolInterface (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): The name of the protocol interface being used for this emulated MLD Host. There may be multiple IPv6 protocol interfaces to select from.NOTE: Only enabled protocol interfaces configured with IPv6 addresses will be listed here.
        - ReportFreq (number): Can be configured only when the Unsolicited Response Mode option is enabled. Otherwise, it is read-only. When Unsolicited Response Mode is enabled, specifies the frequency, in seconds, with which unsolicited messages are generated.
        - RobustnessVariable (number): NOT DEFINED
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        - Version (str(version1 | version2)): Sets the MLD version number that is to be simulated on the host: 1 or 2.

        Returns
        -------
        - self: This instance with matching host resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of host data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the host resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def GetInterfaceAccessorIfaceList(self):
        """Executes the getInterfaceAccessorIfaceList operation on the server.

        Gets the interface accesor Iface list.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('getInterfaceAccessorIfaceList', payload=payload, response_object=None)
