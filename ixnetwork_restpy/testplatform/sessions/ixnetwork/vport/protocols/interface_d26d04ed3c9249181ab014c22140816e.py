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
    """A set of interfaces to be included in the stpBridge object.
    The Interface class encapsulates a list of interface resources that are managed by the user.
    A list of resources can be retrieved from the server using the Interface.find() method.
    The list can be managed by using the Interface.add() and Interface.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'interface'
    _SDM_ATT_MAP = {
        'AutoPick': 'autoPick',
        'BdpuGap': 'bdpuGap',
        'Cost': 'cost',
        'Enabled': 'enabled',
        'InterfaceId': 'interfaceId',
        'JitterEnabled': 'jitterEnabled',
        'JitterPercentage': 'jitterPercentage',
        'LinkType': 'linkType',
        'MstiOrVlanId': 'mstiOrVlanId',
        'PortNo': 'portNo',
        'Pvid': 'pvid',
    }

    def __init__(self, parent):
        super(Interface, self).__init__(parent)

    @property
    def LearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedinfo_79bbbce3444e06c4cd90272042ccc2f7.LearnedInfo): An instance of the LearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedinfo_79bbbce3444e06c4cd90272042ccc2f7 import LearnedInfo
        return LearnedInfo(self)._select()

    @property
    def AutoPick(self):
        """
        Returns
        -------
        - bool: If set, then the Auto-Pick Port Number feature is enabled and each STP interface configured for the same bridge will be assigned a unique port number automatically.(default = enabled)
        """
        return self._get_attribute(self._SDM_ATT_MAP['AutoPick'])
    @AutoPick.setter
    def AutoPick(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AutoPick'], value)

    @property
    def BdpuGap(self):
        """
        Returns
        -------
        - number: The length of time between transmissions of BPDUs, in milliseconds. The valid range is 0 msec to 60,000 msec. (default = 0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['BdpuGap'])
    @BdpuGap.setter
    def BdpuGap(self, value):
        self._set_attribute(self._SDM_ATT_MAP['BdpuGap'], value)

    @property
    def Cost(self):
        """
        Returns
        -------
        - number: The administrative path cost assigned to this interface. The valid range is 0 to 4294967295. (default = 1)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Cost'])
    @Cost.setter
    def Cost(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Cost'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables or disables the use of the interface. (default = disabled)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def InterfaceId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface): The unique identifier for this interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceId'])
    @InterfaceId.setter
    def InterfaceId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceId'], value)

    @property
    def JitterEnabled(self):
        """
        Returns
        -------
        - bool: Staggered transmit (jitter) for Hello messages. If set, then the jitter feature is enabled. (default = enabled)
        """
        return self._get_attribute(self._SDM_ATT_MAP['JitterEnabled'])
    @JitterEnabled.setter
    def JitterEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['JitterEnabled'], value)

    @property
    def JitterPercentage(self):
        """
        Returns
        -------
        - number: The maximum percentage of +/- variation (jitter) from the Hello message transmission interval.
        """
        return self._get_attribute(self._SDM_ATT_MAP['JitterPercentage'])
    @JitterPercentage.setter
    def JitterPercentage(self, value):
        self._set_attribute(self._SDM_ATT_MAP['JitterPercentage'], value)

    @property
    def LinkType(self):
        """
        Returns
        -------
        - str(pointToPoint | shared): The type of link attached to this interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkType'])
    @LinkType.setter
    def LinkType(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LinkType'], value)

    @property
    def MstiOrVlanId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../all | /api/v1/sessions/1/ixnetwork/vport/.../msti | /api/v1/sessions/1/ixnetwork/vport/.../vlan): The identifier for this MSTI or the identifier for the first VLAN in the range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MstiOrVlanId'])
    @MstiOrVlanId.setter
    def MstiOrVlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MstiOrVlanId'], value)

    @property
    def PortNo(self):
        """
        Returns
        -------
        - number: The port number associated with this STP interface. If enableAutoPickPortNum is set, the port number will be automatically assigned (not editable by the user). If enableAutoPickPortNum is not set, the port number can be configured by the user. The valid range is 1 to 4,095. (default = 1)
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortNo'])
    @PortNo.setter
    def PortNo(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortNo'], value)

    @property
    def Pvid(self):
        """
        Returns
        -------
        - number: The Port VLAN ID. This value must be the same for all ports participating in the PVST+/RPVST+ protocol. The valid range is 1 to 4,094. (default = 1)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Pvid'])
    @Pvid.setter
    def Pvid(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Pvid'], value)

    def update(self, AutoPick=None, BdpuGap=None, Cost=None, Enabled=None, InterfaceId=None, JitterEnabled=None, JitterPercentage=None, LinkType=None, MstiOrVlanId=None, PortNo=None, Pvid=None):
        """Updates interface resource on the server.

        Args
        ----
        - AutoPick (bool): If set, then the Auto-Pick Port Number feature is enabled and each STP interface configured for the same bridge will be assigned a unique port number automatically.(default = enabled)
        - BdpuGap (number): The length of time between transmissions of BPDUs, in milliseconds. The valid range is 0 msec to 60,000 msec. (default = 0)
        - Cost (number): The administrative path cost assigned to this interface. The valid range is 0 to 4294967295. (default = 1)
        - Enabled (bool): Enables or disables the use of the interface. (default = disabled)
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): The unique identifier for this interface.
        - JitterEnabled (bool): Staggered transmit (jitter) for Hello messages. If set, then the jitter feature is enabled. (default = enabled)
        - JitterPercentage (number): The maximum percentage of +/- variation (jitter) from the Hello message transmission interval.
        - LinkType (str(pointToPoint | shared)): The type of link attached to this interface.
        - MstiOrVlanId (str(None | /api/v1/sessions/1/ixnetwork/vport/.../all | /api/v1/sessions/1/ixnetwork/vport/.../msti | /api/v1/sessions/1/ixnetwork/vport/.../vlan)): The identifier for this MSTI or the identifier for the first VLAN in the range.
        - PortNo (number): The port number associated with this STP interface. If enableAutoPickPortNum is set, the port number will be automatically assigned (not editable by the user). If enableAutoPickPortNum is not set, the port number can be configured by the user. The valid range is 1 to 4,095. (default = 1)
        - Pvid (number): The Port VLAN ID. This value must be the same for all ports participating in the PVST+/RPVST+ protocol. The valid range is 1 to 4,094. (default = 1)

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AutoPick=None, BdpuGap=None, Cost=None, Enabled=None, InterfaceId=None, JitterEnabled=None, JitterPercentage=None, LinkType=None, MstiOrVlanId=None, PortNo=None, Pvid=None):
        """Adds a new interface resource on the server and adds it to the container.

        Args
        ----
        - AutoPick (bool): If set, then the Auto-Pick Port Number feature is enabled and each STP interface configured for the same bridge will be assigned a unique port number automatically.(default = enabled)
        - BdpuGap (number): The length of time between transmissions of BPDUs, in milliseconds. The valid range is 0 msec to 60,000 msec. (default = 0)
        - Cost (number): The administrative path cost assigned to this interface. The valid range is 0 to 4294967295. (default = 1)
        - Enabled (bool): Enables or disables the use of the interface. (default = disabled)
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): The unique identifier for this interface.
        - JitterEnabled (bool): Staggered transmit (jitter) for Hello messages. If set, then the jitter feature is enabled. (default = enabled)
        - JitterPercentage (number): The maximum percentage of +/- variation (jitter) from the Hello message transmission interval.
        - LinkType (str(pointToPoint | shared)): The type of link attached to this interface.
        - MstiOrVlanId (str(None | /api/v1/sessions/1/ixnetwork/vport/.../all | /api/v1/sessions/1/ixnetwork/vport/.../msti | /api/v1/sessions/1/ixnetwork/vport/.../vlan)): The identifier for this MSTI or the identifier for the first VLAN in the range.
        - PortNo (number): The port number associated with this STP interface. If enableAutoPickPortNum is set, the port number will be automatically assigned (not editable by the user). If enableAutoPickPortNum is not set, the port number can be configured by the user. The valid range is 1 to 4,095. (default = 1)
        - Pvid (number): The Port VLAN ID. This value must be the same for all ports participating in the PVST+/RPVST+ protocol. The valid range is 1 to 4,094. (default = 1)

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

    def find(self, AutoPick=None, BdpuGap=None, Cost=None, Enabled=None, InterfaceId=None, JitterEnabled=None, JitterPercentage=None, LinkType=None, MstiOrVlanId=None, PortNo=None, Pvid=None):
        """Finds and retrieves interface resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve interface resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all interface resources from the server.

        Args
        ----
        - AutoPick (bool): If set, then the Auto-Pick Port Number feature is enabled and each STP interface configured for the same bridge will be assigned a unique port number automatically.(default = enabled)
        - BdpuGap (number): The length of time between transmissions of BPDUs, in milliseconds. The valid range is 0 msec to 60,000 msec. (default = 0)
        - Cost (number): The administrative path cost assigned to this interface. The valid range is 0 to 4294967295. (default = 1)
        - Enabled (bool): Enables or disables the use of the interface. (default = disabled)
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): The unique identifier for this interface.
        - JitterEnabled (bool): Staggered transmit (jitter) for Hello messages. If set, then the jitter feature is enabled. (default = enabled)
        - JitterPercentage (number): The maximum percentage of +/- variation (jitter) from the Hello message transmission interval.
        - LinkType (str(pointToPoint | shared)): The type of link attached to this interface.
        - MstiOrVlanId (str(None | /api/v1/sessions/1/ixnetwork/vport/.../all | /api/v1/sessions/1/ixnetwork/vport/.../msti | /api/v1/sessions/1/ixnetwork/vport/.../vlan)): The identifier for this MSTI or the identifier for the first VLAN in the range.
        - PortNo (number): The port number associated with this STP interface. If enableAutoPickPortNum is set, the port number will be automatically assigned (not editable by the user). If enableAutoPickPortNum is not set, the port number can be configured by the user. The valid range is 1 to 4,095. (default = 1)
        - Pvid (number): The Port VLAN ID. This value must be the same for all ports participating in the PVST+/RPVST+ protocol. The valid range is 1 to 4,094. (default = 1)

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

    def UpdateParameters(self):
        """Executes the updateParameters operation on the server.

        Updates the current STP bridge interface parameters.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('updateParameters', payload=payload, response_object=None)
