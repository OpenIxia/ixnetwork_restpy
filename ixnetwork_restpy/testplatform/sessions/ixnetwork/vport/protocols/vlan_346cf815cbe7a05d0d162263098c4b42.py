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


class Vlan(Base):
    """This object represents a set of STP VLANs for use with PVST+/RPVST.
    The Vlan class encapsulates a list of vlan resources that are managed by the user.
    A list of resources can be retrieved from the server using the Vlan.find() method.
    The list can be managed by using the Vlan.add() and Vlan.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'vlan'
    _SDM_ATT_MAP = {
        'Enabled': 'enabled',
        'InternalRootPathCost': 'internalRootPathCost',
        'Mac': 'mac',
        'PortPriority': 'portPriority',
        'Priority': 'priority',
        'UpdateRequired': 'updateRequired',
        'VlanId': 'vlanId',
    }

    def __init__(self, parent):
        super(Vlan, self).__init__(parent)

    @property
    def LearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedinfo_8d113649213fa2756fbe01251399d4a7.LearnedInfo): An instance of the LearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedinfo_8d113649213fa2756fbe01251399d4a7 import LearnedInfo
        return LearnedInfo(self)._select()

    @property
    def LearnedInterface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedinterface_5c9d203cae9c9266ed5a3c6cd8f67e6e.LearnedInterface): An instance of the LearnedInterface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.learnedinterface_5c9d203cae9c9266ed5a3c6cd8f67e6e import LearnedInterface
        return LearnedInterface(self)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables the use of this STP VLAN. (default = disabled)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def InternalRootPathCost(self):
        """
        Returns
        -------
        - number: Administrative path cost to the root bridge. The default is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InternalRootPathCost'])
    @InternalRootPathCost.setter
    def InternalRootPathCost(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InternalRootPathCost'], value)

    @property
    def Mac(self):
        """
        Returns
        -------
        - str: The 6-byte MAC address of the port. (default = 00:00 :00:00:00:00)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mac'])
    @Mac.setter
    def Mac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Mac'], value)

    @property
    def PortPriority(self):
        """
        Returns
        -------
        - number: The root priority for this port. The valid range is 0 to 61,440, in increments of 4,096. (default = 32,768)
        """
        return self._get_attribute(self._SDM_ATT_MAP['PortPriority'])
    @PortPriority.setter
    def PortPriority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['PortPriority'], value)

    @property
    def Priority(self):
        """
        Returns
        -------
        - str(0 | 4096 | 8192 | 12288 | 16384 | 20480 | 24576 | 28672 | 32768 | 36864 | 40960 | 45056 | 49152 | 53248 | 57344 | 61440): The port priority for the emulated port on this PVST+ or RPVST+ bridge that is connected to the VLAN.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Priority'])
    @Priority.setter
    def Priority(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Priority'], value)

    @property
    def UpdateRequired(self):
        """
        Returns
        -------
        - bool: If true, cause the VLAN to update.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpdateRequired'])
    @UpdateRequired.setter
    def UpdateRequired(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpdateRequired'], value)

    @property
    def VlanId(self):
        """
        Returns
        -------
        - number: The identifier for this VLAN. The valid range is 2 to 4,094. (default = 2)
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanId'])
    @VlanId.setter
    def VlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanId'], value)

    def update(self, Enabled=None, InternalRootPathCost=None, Mac=None, PortPriority=None, Priority=None, UpdateRequired=None, VlanId=None):
        """Updates vlan resource on the server.

        Args
        ----
        - Enabled (bool): Enables the use of this STP VLAN. (default = disabled)
        - InternalRootPathCost (number): Administrative path cost to the root bridge. The default is 0.
        - Mac (str): The 6-byte MAC address of the port. (default = 00:00 :00:00:00:00)
        - PortPriority (number): The root priority for this port. The valid range is 0 to 61,440, in increments of 4,096. (default = 32,768)
        - Priority (str(0 | 4096 | 8192 | 12288 | 16384 | 20480 | 24576 | 28672 | 32768 | 36864 | 40960 | 45056 | 49152 | 53248 | 57344 | 61440)): The port priority for the emulated port on this PVST+ or RPVST+ bridge that is connected to the VLAN.
        - UpdateRequired (bool): If true, cause the VLAN to update.
        - VlanId (number): The identifier for this VLAN. The valid range is 2 to 4,094. (default = 2)

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Enabled=None, InternalRootPathCost=None, Mac=None, PortPriority=None, Priority=None, UpdateRequired=None, VlanId=None):
        """Adds a new vlan resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): Enables the use of this STP VLAN. (default = disabled)
        - InternalRootPathCost (number): Administrative path cost to the root bridge. The default is 0.
        - Mac (str): The 6-byte MAC address of the port. (default = 00:00 :00:00:00:00)
        - PortPriority (number): The root priority for this port. The valid range is 0 to 61,440, in increments of 4,096. (default = 32,768)
        - Priority (str(0 | 4096 | 8192 | 12288 | 16384 | 20480 | 24576 | 28672 | 32768 | 36864 | 40960 | 45056 | 49152 | 53248 | 57344 | 61440)): The port priority for the emulated port on this PVST+ or RPVST+ bridge that is connected to the VLAN.
        - UpdateRequired (bool): If true, cause the VLAN to update.
        - VlanId (number): The identifier for this VLAN. The valid range is 2 to 4,094. (default = 2)

        Returns
        -------
        - self: This instance with all currently retrieved vlan resources using find and the newly added vlan resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained vlan resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, InternalRootPathCost=None, Mac=None, PortPriority=None, Priority=None, UpdateRequired=None, VlanId=None):
        """Finds and retrieves vlan resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve vlan resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all vlan resources from the server.

        Args
        ----
        - Enabled (bool): Enables the use of this STP VLAN. (default = disabled)
        - InternalRootPathCost (number): Administrative path cost to the root bridge. The default is 0.
        - Mac (str): The 6-byte MAC address of the port. (default = 00:00 :00:00:00:00)
        - PortPriority (number): The root priority for this port. The valid range is 0 to 61,440, in increments of 4,096. (default = 32,768)
        - Priority (str(0 | 4096 | 8192 | 12288 | 16384 | 20480 | 24576 | 28672 | 32768 | 36864 | 40960 | 45056 | 49152 | 53248 | 57344 | 61440)): The port priority for the emulated port on this PVST+ or RPVST+ bridge that is connected to the VLAN.
        - UpdateRequired (bool): If true, cause the VLAN to update.
        - VlanId (number): The identifier for this VLAN. The valid range is 2 to 4,094. (default = 2)

        Returns
        -------
        - self: This instance with matching vlan resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of vlan data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the vlan resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def TopologyChange(self):
        """Executes the topologyChange operation on the server.

        This commands checks to see if there has been a topology change for the specified STP VLAN.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('topologyChange', payload=payload, response_object=None)

    def UpdateParameters(self):
        """Executes the updateParameters operation on the server.

        Updates the current STP VLAN parameters.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('updateParameters', payload=payload, response_object=None)
