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


class DceNodeMacGroups(Base):
    """Sets the DCE Node MAC Groups for a particular DCE ISIS Network Range.
    The DceNodeMacGroups class encapsulates a list of dceNodeMacGroups resources that are managed by the user.
    A list of resources can be retrieved from the server using the DceNodeMacGroups.find() method.
    The list can be managed by using the DceNodeMacGroups.add() and DceNodeMacGroups.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dceNodeMacGroups'
    _SDM_ATT_MAP = {
        'IncludeMacGroups': 'includeMacGroups',
        'InterGroupUnicastMacIncrement': 'interGroupUnicastMacIncrement',
        'IntraGroupUnicastMacIncrement': 'intraGroupUnicastMacIncrement',
        'MulticastAddressNodeStep': 'multicastAddressNodeStep',
        'MulticastMacCount': 'multicastMacCount',
        'MulticastMacStep': 'multicastMacStep',
        'NoOfUnicastScrMacsPerMulicastMac': 'noOfUnicastScrMacsPerMulicastMac',
        'SourceGroupMapping': 'sourceGroupMapping',
        'StartMulticastMac': 'startMulticastMac',
        'StartUnicastSourceMac': 'startUnicastSourceMac',
        'UnicastAddressNodeStep': 'unicastAddressNodeStep',
        'VlanId': 'vlanId',
    }

    def __init__(self, parent):
        super(DceNodeMacGroups, self).__init__(parent)

    @property
    def IncludeMacGroups(self):
        """
        Returns
        -------
        - bool: If true, includes MAC groups for this Network Range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeMacGroups'])
    @IncludeMacGroups.setter
    def IncludeMacGroups(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeMacGroups'], value)

    @property
    def InterGroupUnicastMacIncrement(self):
        """
        Returns
        -------
        - str: The MAC address format of the Unicast MAC between one or more node groups.
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
        - str: The MAC address format of the Unicast MAC within a node group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IntraGroupUnicastMacIncrement'])
    @IntraGroupUnicastMacIncrement.setter
    def IntraGroupUnicastMacIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IntraGroupUnicastMacIncrement'], value)

    @property
    def MulticastAddressNodeStep(self):
        """
        Returns
        -------
        - str: The Multicast MAC address that configures the increment across the Network Range simulated RBridges.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MulticastAddressNodeStep'])
    @MulticastAddressNodeStep.setter
    def MulticastAddressNodeStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MulticastAddressNodeStep'], value)

    @property
    def MulticastMacCount(self):
        """
        Returns
        -------
        - number: The number of Multicast MAC addresses.
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
        - str: The incremental value of Multicast MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MulticastMacStep'])
    @MulticastMacStep.setter
    def MulticastMacStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MulticastMacStep'], value)

    @property
    def NoOfUnicastScrMacsPerMulicastMac(self):
        """
        Returns
        -------
        - number: The number of Unicast Source for each Multicast MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfUnicastScrMacsPerMulicastMac'])
    @NoOfUnicastScrMacsPerMulicastMac.setter
    def NoOfUnicastScrMacsPerMulicastMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfUnicastScrMacsPerMulicastMac'], value)

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
        - str: The MAC address format of the starting Multicast MAC.
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
        - str: The MAC address format of the starting Unicast Source MAC.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartUnicastSourceMac'])
    @StartUnicastSourceMac.setter
    def StartUnicastSourceMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartUnicastSourceMac'], value)

    @property
    def UnicastAddressNodeStep(self):
        """
        Returns
        -------
        - str: The Unicast MAC address that configures the increment across the Network Range simulated RBridges.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UnicastAddressNodeStep'])
    @UnicastAddressNodeStep.setter
    def UnicastAddressNodeStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UnicastAddressNodeStep'], value)

    @property
    def VlanId(self):
        """
        Returns
        -------
        - number: The VLAN ID of the enabled Multicast MAC Range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanId'])
    @VlanId.setter
    def VlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanId'], value)

    def update(self, IncludeMacGroups=None, InterGroupUnicastMacIncrement=None, IntraGroupUnicastMacIncrement=None, MulticastAddressNodeStep=None, MulticastMacCount=None, MulticastMacStep=None, NoOfUnicastScrMacsPerMulicastMac=None, SourceGroupMapping=None, StartMulticastMac=None, StartUnicastSourceMac=None, UnicastAddressNodeStep=None, VlanId=None):
        """Updates dceNodeMacGroups resource on the server.

        Args
        ----
        - IncludeMacGroups (bool): If true, includes MAC groups for this Network Range.
        - InterGroupUnicastMacIncrement (str): The MAC address format of the Unicast MAC between one or more node groups.
        - IntraGroupUnicastMacIncrement (str): The MAC address format of the Unicast MAC within a node group.
        - MulticastAddressNodeStep (str): The Multicast MAC address that configures the increment across the Network Range simulated RBridges.
        - MulticastMacCount (number): The number of Multicast MAC addresses.
        - MulticastMacStep (str): The incremental value of Multicast MAC address.
        - NoOfUnicastScrMacsPerMulicastMac (number): The number of Unicast Source for each Multicast MAC address.
        - SourceGroupMapping (str(fullyMeshed | oneToOne | manualMapping)): The Source Group mapping type.
        - StartMulticastMac (str): The MAC address format of the starting Multicast MAC.
        - StartUnicastSourceMac (str): The MAC address format of the starting Unicast Source MAC.
        - UnicastAddressNodeStep (str): The Unicast MAC address that configures the increment across the Network Range simulated RBridges.
        - VlanId (number): The VLAN ID of the enabled Multicast MAC Range.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, IncludeMacGroups=None, InterGroupUnicastMacIncrement=None, IntraGroupUnicastMacIncrement=None, MulticastAddressNodeStep=None, MulticastMacCount=None, MulticastMacStep=None, NoOfUnicastScrMacsPerMulicastMac=None, SourceGroupMapping=None, StartMulticastMac=None, StartUnicastSourceMac=None, UnicastAddressNodeStep=None, VlanId=None):
        """Adds a new dceNodeMacGroups resource on the server and adds it to the container.

        Args
        ----
        - IncludeMacGroups (bool): If true, includes MAC groups for this Network Range.
        - InterGroupUnicastMacIncrement (str): The MAC address format of the Unicast MAC between one or more node groups.
        - IntraGroupUnicastMacIncrement (str): The MAC address format of the Unicast MAC within a node group.
        - MulticastAddressNodeStep (str): The Multicast MAC address that configures the increment across the Network Range simulated RBridges.
        - MulticastMacCount (number): The number of Multicast MAC addresses.
        - MulticastMacStep (str): The incremental value of Multicast MAC address.
        - NoOfUnicastScrMacsPerMulicastMac (number): The number of Unicast Source for each Multicast MAC address.
        - SourceGroupMapping (str(fullyMeshed | oneToOne | manualMapping)): The Source Group mapping type.
        - StartMulticastMac (str): The MAC address format of the starting Multicast MAC.
        - StartUnicastSourceMac (str): The MAC address format of the starting Unicast Source MAC.
        - UnicastAddressNodeStep (str): The Unicast MAC address that configures the increment across the Network Range simulated RBridges.
        - VlanId (number): The VLAN ID of the enabled Multicast MAC Range.

        Returns
        -------
        - self: This instance with all currently retrieved dceNodeMacGroups resources using find and the newly added dceNodeMacGroups resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained dceNodeMacGroups resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, IncludeMacGroups=None, InterGroupUnicastMacIncrement=None, IntraGroupUnicastMacIncrement=None, MulticastAddressNodeStep=None, MulticastMacCount=None, MulticastMacStep=None, NoOfUnicastScrMacsPerMulicastMac=None, SourceGroupMapping=None, StartMulticastMac=None, StartUnicastSourceMac=None, UnicastAddressNodeStep=None, VlanId=None):
        """Finds and retrieves dceNodeMacGroups resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dceNodeMacGroups resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dceNodeMacGroups resources from the server.

        Args
        ----
        - IncludeMacGroups (bool): If true, includes MAC groups for this Network Range.
        - InterGroupUnicastMacIncrement (str): The MAC address format of the Unicast MAC between one or more node groups.
        - IntraGroupUnicastMacIncrement (str): The MAC address format of the Unicast MAC within a node group.
        - MulticastAddressNodeStep (str): The Multicast MAC address that configures the increment across the Network Range simulated RBridges.
        - MulticastMacCount (number): The number of Multicast MAC addresses.
        - MulticastMacStep (str): The incremental value of Multicast MAC address.
        - NoOfUnicastScrMacsPerMulicastMac (number): The number of Unicast Source for each Multicast MAC address.
        - SourceGroupMapping (str(fullyMeshed | oneToOne | manualMapping)): The Source Group mapping type.
        - StartMulticastMac (str): The MAC address format of the starting Multicast MAC.
        - StartUnicastSourceMac (str): The MAC address format of the starting Unicast Source MAC.
        - UnicastAddressNodeStep (str): The Unicast MAC address that configures the increment across the Network Range simulated RBridges.
        - VlanId (number): The VLAN ID of the enabled Multicast MAC Range.

        Returns
        -------
        - self: This instance with matching dceNodeMacGroups resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dceNodeMacGroups data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dceNodeMacGroups resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
