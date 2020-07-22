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


class DceNodeIpv6Groups(Base):
    """Sets the DCE Node IPv6 Groups for a particular DCE ISIS Network Range.
    The DceNodeIpv6Groups class encapsulates a list of dceNodeIpv6Groups resources that are managed by the user.
    A list of resources can be retrieved from the server using the DceNodeIpv6Groups.find() method.
    The list can be managed by using the DceNodeIpv6Groups.add() and DceNodeIpv6Groups.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dceNodeIpv6Groups'
    _SDM_ATT_MAP = {
        'IncludeIpv6Groups': 'includeIpv6Groups',
        'InterGroupUnicastIpv6Increment': 'interGroupUnicastIpv6Increment',
        'IntraGroupUnicastIpv6Increment': 'intraGroupUnicastIpv6Increment',
        'MulticastAddressNodeStep': 'multicastAddressNodeStep',
        'MulticastIpv6Count': 'multicastIpv6Count',
        'MulticastIpv6Step': 'multicastIpv6Step',
        'NoOfUnicastScrIpv6sPerMulicastIpv6': 'noOfUnicastScrIpv6sPerMulicastIpv6',
        'SourceGroupMapping': 'sourceGroupMapping',
        'StartMulticastIpv6': 'startMulticastIpv6',
        'StartUnicastSourceIpv6': 'startUnicastSourceIpv6',
        'UnicastAddressNodeStep': 'unicastAddressNodeStep',
        'VlanId': 'vlanId',
    }

    def __init__(self, parent):
        super(DceNodeIpv6Groups, self).__init__(parent)

    @property
    def IncludeIpv6Groups(self):
        """
        Returns
        -------
        - bool: If true, includes IPv6 groups for this Network Range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeIpv6Groups'])
    @IncludeIpv6Groups.setter
    def IncludeIpv6Groups(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeIpv6Groups'], value)

    @property
    def InterGroupUnicastIpv6Increment(self):
        """
        Returns
        -------
        - str: The IPv6 address format of the Unicast IPv6 between one or more node groups.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterGroupUnicastIpv6Increment'])
    @InterGroupUnicastIpv6Increment.setter
    def InterGroupUnicastIpv6Increment(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterGroupUnicastIpv6Increment'], value)

    @property
    def IntraGroupUnicastIpv6Increment(self):
        """
        Returns
        -------
        - str: The IPv6 address format of the Unicast MAC within a node group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IntraGroupUnicastIpv6Increment'])
    @IntraGroupUnicastIpv6Increment.setter
    def IntraGroupUnicastIpv6Increment(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IntraGroupUnicastIpv6Increment'], value)

    @property
    def MulticastAddressNodeStep(self):
        """
        Returns
        -------
        - str: The Multicast IPv6 address that configures the increment across the Network Range simulated RBridges.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MulticastAddressNodeStep'])
    @MulticastAddressNodeStep.setter
    def MulticastAddressNodeStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MulticastAddressNodeStep'], value)

    @property
    def MulticastIpv6Count(self):
        """
        Returns
        -------
        - number: The number of Multicast IPv6 addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MulticastIpv6Count'])
    @MulticastIpv6Count.setter
    def MulticastIpv6Count(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MulticastIpv6Count'], value)

    @property
    def MulticastIpv6Step(self):
        """
        Returns
        -------
        - str: The incremental value of Multicast IPv6 address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MulticastIpv6Step'])
    @MulticastIpv6Step.setter
    def MulticastIpv6Step(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MulticastIpv6Step'], value)

    @property
    def NoOfUnicastScrIpv6sPerMulicastIpv6(self):
        """
        Returns
        -------
        - number: The number of Unicast Source for each Multicast IPv6 address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfUnicastScrIpv6sPerMulicastIpv6'])
    @NoOfUnicastScrIpv6sPerMulicastIpv6.setter
    def NoOfUnicastScrIpv6sPerMulicastIpv6(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfUnicastScrIpv6sPerMulicastIpv6'], value)

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
    def StartMulticastIpv6(self):
        """
        Returns
        -------
        - str: The IP address format of the starting Multicast IPv6 address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartMulticastIpv6'])
    @StartMulticastIpv6.setter
    def StartMulticastIpv6(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartMulticastIpv6'], value)

    @property
    def StartUnicastSourceIpv6(self):
        """
        Returns
        -------
        - str: The IPv6 address format of the starting Unicast Source IPv6.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartUnicastSourceIpv6'])
    @StartUnicastSourceIpv6.setter
    def StartUnicastSourceIpv6(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartUnicastSourceIpv6'], value)

    @property
    def UnicastAddressNodeStep(self):
        """
        Returns
        -------
        - str: The Unicast IPv6 address that configures the increment across the Network Range simulated RBridges.
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
        - number: The VLAN ID of the enabled Multicast IPv6 Group Range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanId'])
    @VlanId.setter
    def VlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanId'], value)

    def update(self, IncludeIpv6Groups=None, InterGroupUnicastIpv6Increment=None, IntraGroupUnicastIpv6Increment=None, MulticastAddressNodeStep=None, MulticastIpv6Count=None, MulticastIpv6Step=None, NoOfUnicastScrIpv6sPerMulicastIpv6=None, SourceGroupMapping=None, StartMulticastIpv6=None, StartUnicastSourceIpv6=None, UnicastAddressNodeStep=None, VlanId=None):
        """Updates dceNodeIpv6Groups resource on the server.

        Args
        ----
        - IncludeIpv6Groups (bool): If true, includes IPv6 groups for this Network Range.
        - InterGroupUnicastIpv6Increment (str): The IPv6 address format of the Unicast IPv6 between one or more node groups.
        - IntraGroupUnicastIpv6Increment (str): The IPv6 address format of the Unicast MAC within a node group.
        - MulticastAddressNodeStep (str): The Multicast IPv6 address that configures the increment across the Network Range simulated RBridges.
        - MulticastIpv6Count (number): The number of Multicast IPv6 addresses.
        - MulticastIpv6Step (str): The incremental value of Multicast IPv6 address.
        - NoOfUnicastScrIpv6sPerMulicastIpv6 (number): The number of Unicast Source for each Multicast IPv6 address.
        - SourceGroupMapping (str(fullyMeshed | oneToOne | manualMapping)): The Source Group mapping type.
        - StartMulticastIpv6 (str): The IP address format of the starting Multicast IPv6 address.
        - StartUnicastSourceIpv6 (str): The IPv6 address format of the starting Unicast Source IPv6.
        - UnicastAddressNodeStep (str): The Unicast IPv6 address that configures the increment across the Network Range simulated RBridges.
        - VlanId (number): The VLAN ID of the enabled Multicast IPv6 Group Range.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, IncludeIpv6Groups=None, InterGroupUnicastIpv6Increment=None, IntraGroupUnicastIpv6Increment=None, MulticastAddressNodeStep=None, MulticastIpv6Count=None, MulticastIpv6Step=None, NoOfUnicastScrIpv6sPerMulicastIpv6=None, SourceGroupMapping=None, StartMulticastIpv6=None, StartUnicastSourceIpv6=None, UnicastAddressNodeStep=None, VlanId=None):
        """Adds a new dceNodeIpv6Groups resource on the server and adds it to the container.

        Args
        ----
        - IncludeIpv6Groups (bool): If true, includes IPv6 groups for this Network Range.
        - InterGroupUnicastIpv6Increment (str): The IPv6 address format of the Unicast IPv6 between one or more node groups.
        - IntraGroupUnicastIpv6Increment (str): The IPv6 address format of the Unicast MAC within a node group.
        - MulticastAddressNodeStep (str): The Multicast IPv6 address that configures the increment across the Network Range simulated RBridges.
        - MulticastIpv6Count (number): The number of Multicast IPv6 addresses.
        - MulticastIpv6Step (str): The incremental value of Multicast IPv6 address.
        - NoOfUnicastScrIpv6sPerMulicastIpv6 (number): The number of Unicast Source for each Multicast IPv6 address.
        - SourceGroupMapping (str(fullyMeshed | oneToOne | manualMapping)): The Source Group mapping type.
        - StartMulticastIpv6 (str): The IP address format of the starting Multicast IPv6 address.
        - StartUnicastSourceIpv6 (str): The IPv6 address format of the starting Unicast Source IPv6.
        - UnicastAddressNodeStep (str): The Unicast IPv6 address that configures the increment across the Network Range simulated RBridges.
        - VlanId (number): The VLAN ID of the enabled Multicast IPv6 Group Range.

        Returns
        -------
        - self: This instance with all currently retrieved dceNodeIpv6Groups resources using find and the newly added dceNodeIpv6Groups resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained dceNodeIpv6Groups resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, IncludeIpv6Groups=None, InterGroupUnicastIpv6Increment=None, IntraGroupUnicastIpv6Increment=None, MulticastAddressNodeStep=None, MulticastIpv6Count=None, MulticastIpv6Step=None, NoOfUnicastScrIpv6sPerMulicastIpv6=None, SourceGroupMapping=None, StartMulticastIpv6=None, StartUnicastSourceIpv6=None, UnicastAddressNodeStep=None, VlanId=None):
        """Finds and retrieves dceNodeIpv6Groups resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dceNodeIpv6Groups resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dceNodeIpv6Groups resources from the server.

        Args
        ----
        - IncludeIpv6Groups (bool): If true, includes IPv6 groups for this Network Range.
        - InterGroupUnicastIpv6Increment (str): The IPv6 address format of the Unicast IPv6 between one or more node groups.
        - IntraGroupUnicastIpv6Increment (str): The IPv6 address format of the Unicast MAC within a node group.
        - MulticastAddressNodeStep (str): The Multicast IPv6 address that configures the increment across the Network Range simulated RBridges.
        - MulticastIpv6Count (number): The number of Multicast IPv6 addresses.
        - MulticastIpv6Step (str): The incremental value of Multicast IPv6 address.
        - NoOfUnicastScrIpv6sPerMulicastIpv6 (number): The number of Unicast Source for each Multicast IPv6 address.
        - SourceGroupMapping (str(fullyMeshed | oneToOne | manualMapping)): The Source Group mapping type.
        - StartMulticastIpv6 (str): The IP address format of the starting Multicast IPv6 address.
        - StartUnicastSourceIpv6 (str): The IPv6 address format of the starting Unicast Source IPv6.
        - UnicastAddressNodeStep (str): The Unicast IPv6 address that configures the increment across the Network Range simulated RBridges.
        - VlanId (number): The VLAN ID of the enabled Multicast IPv6 Group Range.

        Returns
        -------
        - self: This instance with matching dceNodeIpv6Groups resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dceNodeIpv6Groups data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dceNodeIpv6Groups resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
