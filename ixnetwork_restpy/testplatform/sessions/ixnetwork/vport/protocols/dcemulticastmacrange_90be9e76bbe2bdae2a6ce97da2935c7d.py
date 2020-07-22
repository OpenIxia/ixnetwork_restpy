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


class DceMulticastMacRange(Base):
    """Sets the Multicast MAC Range for the DCE ISIS router.
    The DceMulticastMacRange class encapsulates a list of dceMulticastMacRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the DceMulticastMacRange.find() method.
    The list can be managed by using the DceMulticastMacRange.add() and DceMulticastMacRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dceMulticastMacRange'
    _SDM_ATT_MAP = {
        'Enabled': 'enabled',
        'InterGroupUnicastMacIncrement': 'interGroupUnicastMacIncrement',
        'IntraGroupUnicastMacIncrement': 'intraGroupUnicastMacIncrement',
        'MulticastMacCount': 'multicastMacCount',
        'MulticastMacStep': 'multicastMacStep',
        'SourceGroupMapping': 'sourceGroupMapping',
        'StartMulticastMac': 'startMulticastMac',
        'StartUnicastSourceMac': 'startUnicastSourceMac',
        'Topology': 'topology',
        'UnicastSourcesPerMulticastMac': 'unicastSourcesPerMulticastMac',
        'VlanId': 'vlanId',
    }

    def __init__(self, parent):
        super(DceMulticastMacRange, self).__init__(parent)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, enables the Multicast MAC Range for a particular DCE ISIS route range. (default = false)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def InterGroupUnicastMacIncrement(self):
        """
        Returns
        -------
        - str: The MAC address format of the Unicast MAC between one or more node groups. (Default = 00 00 00 00 00)
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterGroupUnicastMacIncrement'])
    @InterGroupUnicastMacIncrement.setter
    def InterGroupUnicastMacIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterGroupUnicastMacIncrement'], value)

    @property
    def IntraGroupUnicastMacIncrement(self):
        """
        Returns
        -------
        - str: The MAC address format of the Unicast MAC within a node group. (Default = 00 00 00 00 01)
        """
        return self._get_attribute(self._SDM_ATT_MAP['IntraGroupUnicastMacIncrement'])
    @IntraGroupUnicastMacIncrement.setter
    def IntraGroupUnicastMacIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IntraGroupUnicastMacIncrement'], value)

    @property
    def MulticastMacCount(self):
        """
        Returns
        -------
        - number: The number of Multicast MAC addresses. This option takes unsigned integer value ranging from 1 to UINT_MAX.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MulticastMacCount'])
    @MulticastMacCount.setter
    def MulticastMacCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MulticastMacCount'], value)

    @property
    def MulticastMacStep(self):
        """
        Returns
        -------
        - str: The incremental value of Multicast MAC address. (Default = 00 00 00 00 01)
        """
        return self._get_attribute(self._SDM_ATT_MAP['MulticastMacStep'])
    @MulticastMacStep.setter
    def MulticastMacStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MulticastMacStep'], value)

    @property
    def SourceGroupMapping(self):
        """
        Returns
        -------
        - str(fullyMeshed | oneToOne | manualMapping): The Source Group mapping type.
        """
        return self._get_attribute(self._SDM_ATT_MAP['SourceGroupMapping'])
    @SourceGroupMapping.setter
    def SourceGroupMapping(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SourceGroupMapping'], value)

    @property
    def StartMulticastMac(self):
        """
        Returns
        -------
        - str: The MAC address format of the starting Multicast MAC. (Default = 0x01000000)
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartMulticastMac'])
    @StartMulticastMac.setter
    def StartMulticastMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartMulticastMac'], value)

    @property
    def StartUnicastSourceMac(self):
        """
        Returns
        -------
        - str: The MAC address format of the starting Unicast Source MAC. (Default = 00 00 00 00 00 00)
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartUnicastSourceMac'])
    @StartUnicastSourceMac.setter
    def StartUnicastSourceMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartUnicastSourceMac'], value)

    @property
    def Topology(self):
        """
        Returns
        -------
        - number: The topology identifier to which the corresponding MAC belongs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Topology'])
    @Topology.setter
    def Topology(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Topology'], value)

    @property
    def UnicastSourcesPerMulticastMac(self):
        """
        Returns
        -------
        - number: The number of Unicast Source for each Multicast MAC address. This option takes unsigned integer value ranging from 0 to UINT_MAX.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UnicastSourcesPerMulticastMac'])
    @UnicastSourcesPerMulticastMac.setter
    def UnicastSourcesPerMulticastMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UnicastSourcesPerMulticastMac'], value)

    @property
    def VlanId(self):
        """
        Returns
        -------
        - number: The VLAN ID of the enabled Multicast MAC Range. (default = 1)
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanId'])
    @VlanId.setter
    def VlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanId'], value)

    def update(self, Enabled=None, InterGroupUnicastMacIncrement=None, IntraGroupUnicastMacIncrement=None, MulticastMacCount=None, MulticastMacStep=None, SourceGroupMapping=None, StartMulticastMac=None, StartUnicastSourceMac=None, Topology=None, UnicastSourcesPerMulticastMac=None, VlanId=None):
        """Updates dceMulticastMacRange resource on the server.

        Args
        ----
        - Enabled (bool): If true, enables the Multicast MAC Range for a particular DCE ISIS route range. (default = false)
        - InterGroupUnicastMacIncrement (str): The MAC address format of the Unicast MAC between one or more node groups. (Default = 00 00 00 00 00)
        - IntraGroupUnicastMacIncrement (str): The MAC address format of the Unicast MAC within a node group. (Default = 00 00 00 00 01)
        - MulticastMacCount (number): The number of Multicast MAC addresses. This option takes unsigned integer value ranging from 1 to UINT_MAX.
        - MulticastMacStep (str): The incremental value of Multicast MAC address. (Default = 00 00 00 00 01)
        - SourceGroupMapping (str(fullyMeshed | oneToOne | manualMapping)): The Source Group mapping type.
        - StartMulticastMac (str): The MAC address format of the starting Multicast MAC. (Default = 0x01000000)
        - StartUnicastSourceMac (str): The MAC address format of the starting Unicast Source MAC. (Default = 00 00 00 00 00 00)
        - Topology (number): The topology identifier to which the corresponding MAC belongs.
        - UnicastSourcesPerMulticastMac (number): The number of Unicast Source for each Multicast MAC address. This option takes unsigned integer value ranging from 0 to UINT_MAX.
        - VlanId (number): The VLAN ID of the enabled Multicast MAC Range. (default = 1)

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Enabled=None, InterGroupUnicastMacIncrement=None, IntraGroupUnicastMacIncrement=None, MulticastMacCount=None, MulticastMacStep=None, SourceGroupMapping=None, StartMulticastMac=None, StartUnicastSourceMac=None, Topology=None, UnicastSourcesPerMulticastMac=None, VlanId=None):
        """Adds a new dceMulticastMacRange resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): If true, enables the Multicast MAC Range for a particular DCE ISIS route range. (default = false)
        - InterGroupUnicastMacIncrement (str): The MAC address format of the Unicast MAC between one or more node groups. (Default = 00 00 00 00 00)
        - IntraGroupUnicastMacIncrement (str): The MAC address format of the Unicast MAC within a node group. (Default = 00 00 00 00 01)
        - MulticastMacCount (number): The number of Multicast MAC addresses. This option takes unsigned integer value ranging from 1 to UINT_MAX.
        - MulticastMacStep (str): The incremental value of Multicast MAC address. (Default = 00 00 00 00 01)
        - SourceGroupMapping (str(fullyMeshed | oneToOne | manualMapping)): The Source Group mapping type.
        - StartMulticastMac (str): The MAC address format of the starting Multicast MAC. (Default = 0x01000000)
        - StartUnicastSourceMac (str): The MAC address format of the starting Unicast Source MAC. (Default = 00 00 00 00 00 00)
        - Topology (number): The topology identifier to which the corresponding MAC belongs.
        - UnicastSourcesPerMulticastMac (number): The number of Unicast Source for each Multicast MAC address. This option takes unsigned integer value ranging from 0 to UINT_MAX.
        - VlanId (number): The VLAN ID of the enabled Multicast MAC Range. (default = 1)

        Returns
        -------
        - self: This instance with all currently retrieved dceMulticastMacRange resources using find and the newly added dceMulticastMacRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained dceMulticastMacRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, InterGroupUnicastMacIncrement=None, IntraGroupUnicastMacIncrement=None, MulticastMacCount=None, MulticastMacStep=None, SourceGroupMapping=None, StartMulticastMac=None, StartUnicastSourceMac=None, Topology=None, UnicastSourcesPerMulticastMac=None, VlanId=None):
        """Finds and retrieves dceMulticastMacRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dceMulticastMacRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dceMulticastMacRange resources from the server.

        Args
        ----
        - Enabled (bool): If true, enables the Multicast MAC Range for a particular DCE ISIS route range. (default = false)
        - InterGroupUnicastMacIncrement (str): The MAC address format of the Unicast MAC between one or more node groups. (Default = 00 00 00 00 00)
        - IntraGroupUnicastMacIncrement (str): The MAC address format of the Unicast MAC within a node group. (Default = 00 00 00 00 01)
        - MulticastMacCount (number): The number of Multicast MAC addresses. This option takes unsigned integer value ranging from 1 to UINT_MAX.
        - MulticastMacStep (str): The incremental value of Multicast MAC address. (Default = 00 00 00 00 01)
        - SourceGroupMapping (str(fullyMeshed | oneToOne | manualMapping)): The Source Group mapping type.
        - StartMulticastMac (str): The MAC address format of the starting Multicast MAC. (Default = 0x01000000)
        - StartUnicastSourceMac (str): The MAC address format of the starting Unicast Source MAC. (Default = 00 00 00 00 00 00)
        - Topology (number): The topology identifier to which the corresponding MAC belongs.
        - UnicastSourcesPerMulticastMac (number): The number of Unicast Source for each Multicast MAC address. This option takes unsigned integer value ranging from 0 to UINT_MAX.
        - VlanId (number): The VLAN ID of the enabled Multicast MAC Range. (default = 1)

        Returns
        -------
        - self: This instance with matching dceMulticastMacRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dceMulticastMacRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dceMulticastMacRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
