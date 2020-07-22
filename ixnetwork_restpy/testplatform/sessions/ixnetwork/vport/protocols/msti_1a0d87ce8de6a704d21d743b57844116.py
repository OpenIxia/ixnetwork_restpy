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


class Msti(Base):
    """A set of MSTIs to be included in stpBridge object.
    The Msti class encapsulates a list of msti resources that are managed by the user.
    A list of resources can be retrieved from the server using the Msti.find() method.
    The list can be managed by using the Msti.add() and Msti.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'msti'
    _SDM_ATT_MAP = {
        'Enabled': 'enabled',
        'InternalRootPathCost': 'internalRootPathCost',
        'Mac': 'mac',
        'MstiHops': 'mstiHops',
        'MstiId': 'mstiId',
        'MstiName': 'mstiName',
        'PortPriority': 'portPriority',
        'Priority': 'priority',
        'UpdateRequired': 'updateRequired',
        'VlanStart': 'vlanStart',
        'VlanStop': 'vlanStop',
    }

    def __init__(self, parent):
        super(Msti, self).__init__(parent)

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
        - bool: Enables the use of this MSTP MSTI. (default = disabled)
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
        - number: The MSTI Internal Root Path Cost. A 4-byte unsigned integer. (default is 0)
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
        - str: The 6-byte MAC address for the MSTI root. This is part of the MSTI regional root identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Mac'])
    @Mac.setter
    def Mac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Mac'], value)

    @property
    def MstiHops(self):
        """
        Returns
        -------
        - number: The number of MSTI hops remaining. An unsigned integer. The valid range is 1 to 255. (default = 20)
        """
        return self._get_attribute(self._SDM_ATT_MAP['MstiHops'])
    @MstiHops.setter
    def MstiHops(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MstiHops'], value)

    @property
    def MstiId(self):
        """
        Returns
        -------
        - number: The identifier for this MST Instance (MSTI). The valid range is 1 to 4,094. (default = 1)
        """
        return self._get_attribute(self._SDM_ATT_MAP['MstiId'])
    @MstiId.setter
    def MstiId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MstiId'], value)

    @property
    def MstiName(self):
        """
        Returns
        -------
        - str: The name of the MSTI which is configured from the list of MSTIs. Format: MSTI ID-n. (Editable by the user.)
        """
        return self._get_attribute(self._SDM_ATT_MAP['MstiName'])
    @MstiName.setter
    def MstiName(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MstiName'], value)

    @property
    def PortPriority(self):
        """
        Returns
        -------
        - str(0 | 16 | 32 | 48 | 64 | 80 | 96 | 112 | 128 | 144 | 160 | 176 | 192 | 208 | 224 | 240): The MSTI Port Priority. This is part of the MSTI Regional Root Identifier. An unsigned integer; a multiple of 16. The valid range is 0 to 240. (default = 0)
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
        - str(0 | 4096 | 8192 | 12288 | 16384 | 20480 | 24576 | 28672 | 32768 | 36864 | 40960 | 45056 | 49152 | 53248 | 57344 | 61440): The MSTI Root Priority. This is part of the MSTI Regional Root Identifier. Since MAC address reduction is used, only multiples of 4096 are used.
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
        - bool: If true, causes the MSTI to update.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UpdateRequired'])
    @UpdateRequired.setter
    def UpdateRequired(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UpdateRequired'], value)

    @property
    def VlanStart(self):
        """
        Returns
        -------
        - number: The ID for the first VLAN in the VLAN range to which the MSTI is mapped. An unsigned integer. Valid range: 1 to 4094.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanStart'])
    @VlanStart.setter
    def VlanStart(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanStart'], value)

    @property
    def VlanStop(self):
        """
        Returns
        -------
        - number: The ID for the last VLAN in the VLAN range to which the MSTI is mapped. An unsigned integer. Valid range: 1 to 4094.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanStop'])
    @VlanStop.setter
    def VlanStop(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanStop'], value)

    def update(self, Enabled=None, InternalRootPathCost=None, Mac=None, MstiHops=None, MstiId=None, MstiName=None, PortPriority=None, Priority=None, UpdateRequired=None, VlanStart=None, VlanStop=None):
        """Updates msti resource on the server.

        Args
        ----
        - Enabled (bool): Enables the use of this MSTP MSTI. (default = disabled)
        - InternalRootPathCost (number): The MSTI Internal Root Path Cost. A 4-byte unsigned integer. (default is 0)
        - Mac (str): The 6-byte MAC address for the MSTI root. This is part of the MSTI regional root identifier.
        - MstiHops (number): The number of MSTI hops remaining. An unsigned integer. The valid range is 1 to 255. (default = 20)
        - MstiId (number): The identifier for this MST Instance (MSTI). The valid range is 1 to 4,094. (default = 1)
        - MstiName (str): The name of the MSTI which is configured from the list of MSTIs. Format: MSTI ID-n. (Editable by the user.)
        - PortPriority (str(0 | 16 | 32 | 48 | 64 | 80 | 96 | 112 | 128 | 144 | 160 | 176 | 192 | 208 | 224 | 240)): The MSTI Port Priority. This is part of the MSTI Regional Root Identifier. An unsigned integer; a multiple of 16. The valid range is 0 to 240. (default = 0)
        - Priority (str(0 | 4096 | 8192 | 12288 | 16384 | 20480 | 24576 | 28672 | 32768 | 36864 | 40960 | 45056 | 49152 | 53248 | 57344 | 61440)): The MSTI Root Priority. This is part of the MSTI Regional Root Identifier. Since MAC address reduction is used, only multiples of 4096 are used.
        - UpdateRequired (bool): If true, causes the MSTI to update.
        - VlanStart (number): The ID for the first VLAN in the VLAN range to which the MSTI is mapped. An unsigned integer. Valid range: 1 to 4094.
        - VlanStop (number): The ID for the last VLAN in the VLAN range to which the MSTI is mapped. An unsigned integer. Valid range: 1 to 4094.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Enabled=None, InternalRootPathCost=None, Mac=None, MstiHops=None, MstiId=None, MstiName=None, PortPriority=None, Priority=None, UpdateRequired=None, VlanStart=None, VlanStop=None):
        """Adds a new msti resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): Enables the use of this MSTP MSTI. (default = disabled)
        - InternalRootPathCost (number): The MSTI Internal Root Path Cost. A 4-byte unsigned integer. (default is 0)
        - Mac (str): The 6-byte MAC address for the MSTI root. This is part of the MSTI regional root identifier.
        - MstiHops (number): The number of MSTI hops remaining. An unsigned integer. The valid range is 1 to 255. (default = 20)
        - MstiId (number): The identifier for this MST Instance (MSTI). The valid range is 1 to 4,094. (default = 1)
        - MstiName (str): The name of the MSTI which is configured from the list of MSTIs. Format: MSTI ID-n. (Editable by the user.)
        - PortPriority (str(0 | 16 | 32 | 48 | 64 | 80 | 96 | 112 | 128 | 144 | 160 | 176 | 192 | 208 | 224 | 240)): The MSTI Port Priority. This is part of the MSTI Regional Root Identifier. An unsigned integer; a multiple of 16. The valid range is 0 to 240. (default = 0)
        - Priority (str(0 | 4096 | 8192 | 12288 | 16384 | 20480 | 24576 | 28672 | 32768 | 36864 | 40960 | 45056 | 49152 | 53248 | 57344 | 61440)): The MSTI Root Priority. This is part of the MSTI Regional Root Identifier. Since MAC address reduction is used, only multiples of 4096 are used.
        - UpdateRequired (bool): If true, causes the MSTI to update.
        - VlanStart (number): The ID for the first VLAN in the VLAN range to which the MSTI is mapped. An unsigned integer. Valid range: 1 to 4094.
        - VlanStop (number): The ID for the last VLAN in the VLAN range to which the MSTI is mapped. An unsigned integer. Valid range: 1 to 4094.

        Returns
        -------
        - self: This instance with all currently retrieved msti resources using find and the newly added msti resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained msti resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, InternalRootPathCost=None, Mac=None, MstiHops=None, MstiId=None, MstiName=None, PortPriority=None, Priority=None, UpdateRequired=None, VlanStart=None, VlanStop=None):
        """Finds and retrieves msti resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve msti resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all msti resources from the server.

        Args
        ----
        - Enabled (bool): Enables the use of this MSTP MSTI. (default = disabled)
        - InternalRootPathCost (number): The MSTI Internal Root Path Cost. A 4-byte unsigned integer. (default is 0)
        - Mac (str): The 6-byte MAC address for the MSTI root. This is part of the MSTI regional root identifier.
        - MstiHops (number): The number of MSTI hops remaining. An unsigned integer. The valid range is 1 to 255. (default = 20)
        - MstiId (number): The identifier for this MST Instance (MSTI). The valid range is 1 to 4,094. (default = 1)
        - MstiName (str): The name of the MSTI which is configured from the list of MSTIs. Format: MSTI ID-n. (Editable by the user.)
        - PortPriority (str(0 | 16 | 32 | 48 | 64 | 80 | 96 | 112 | 128 | 144 | 160 | 176 | 192 | 208 | 224 | 240)): The MSTI Port Priority. This is part of the MSTI Regional Root Identifier. An unsigned integer; a multiple of 16. The valid range is 0 to 240. (default = 0)
        - Priority (str(0 | 4096 | 8192 | 12288 | 16384 | 20480 | 24576 | 28672 | 32768 | 36864 | 40960 | 45056 | 49152 | 53248 | 57344 | 61440)): The MSTI Root Priority. This is part of the MSTI Regional Root Identifier. Since MAC address reduction is used, only multiples of 4096 are used.
        - UpdateRequired (bool): If true, causes the MSTI to update.
        - VlanStart (number): The ID for the first VLAN in the VLAN range to which the MSTI is mapped. An unsigned integer. Valid range: 1 to 4094.
        - VlanStop (number): The ID for the last VLAN in the VLAN range to which the MSTI is mapped. An unsigned integer. Valid range: 1 to 4094.

        Returns
        -------
        - self: This instance with matching msti resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of msti data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the msti resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def TopologyChange(self):
        """Executes the topologyChange operation on the server.

        This command checks to see if a topology change has occurred on the specified STP bridge MSTI.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('topologyChange', payload=payload, response_object=None)

    def UpdateParameters(self):
        """Executes the updateParameters operation on the server.

        Updates the current STP parameters on the specified bridge MSTI.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        return self._execute('updateParameters', payload=payload, response_object=None)
