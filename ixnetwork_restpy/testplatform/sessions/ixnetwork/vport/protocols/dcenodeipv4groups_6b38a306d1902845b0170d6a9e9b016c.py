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


class DceNodeIpv4Groups(Base):
    """Sets the DCE Node IPv4 Groups for a particular DCE ISIS Network Range.
    The DceNodeIpv4Groups class encapsulates a list of dceNodeIpv4Groups resources that are managed by the user.
    A list of resources can be retrieved from the server using the DceNodeIpv4Groups.find() method.
    The list can be managed by using the DceNodeIpv4Groups.add() and DceNodeIpv4Groups.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dceNodeIpv4Groups'
    _SDM_ATT_MAP = {
        'IncludeIpv4Groups': 'includeIpv4Groups',
        'InterGroupUnicastIpv4Increment': 'interGroupUnicastIpv4Increment',
        'IntraGroupUnicastIpv4Increment': 'intraGroupUnicastIpv4Increment',
        'MulticastAddressNodeStep': 'multicastAddressNodeStep',
        'MulticastIpv4Count': 'multicastIpv4Count',
        'MulticastIpv4Step': 'multicastIpv4Step',
        'NoOfUnicastScrIpv4sPerMulicastIpv4': 'noOfUnicastScrIpv4sPerMulicastIpv4',
        'SourceGroupMapping': 'sourceGroupMapping',
        'StartMulticastIpv4': 'startMulticastIpv4',
        'StartUnicastSourceIpv4': 'startUnicastSourceIpv4',
        'UnicastAddressNodeStep': 'unicastAddressNodeStep',
        'VlanId': 'vlanId',
    }

    def __init__(self, parent):
        super(DceNodeIpv4Groups, self).__init__(parent)

    @property
    def IncludeIpv4Groups(self):
        """
        Returns
        -------
        - bool: If true, includes IPv4 groups for this Network Range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeIpv4Groups'])
    @IncludeIpv4Groups.setter
    def IncludeIpv4Groups(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeIpv4Groups'], value)

    @property
    def InterGroupUnicastIpv4Increment(self):
        """
        Returns
        -------
        - str: The IPv4 address format of the Unicast IPv4 between one or more node groups.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterGroupUnicastIpv4Increment'])
    @InterGroupUnicastIpv4Increment.setter
    def InterGroupUnicastIpv4Increment(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterGroupUnicastIpv4Increment'], value)

    @property
    def IntraGroupUnicastIpv4Increment(self):
        """
        Returns
        -------
        - str: The IPv4 address format of the Unicast MAC within a node group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IntraGroupUnicastIpv4Increment'])
    @IntraGroupUnicastIpv4Increment.setter
    def IntraGroupUnicastIpv4Increment(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IntraGroupUnicastIpv4Increment'], value)

    @property
    def MulticastAddressNodeStep(self):
        """
        Returns
        -------
        - str: The Multicast IPv4 address that configures the increment across the Network Range simulated RBridges.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MulticastAddressNodeStep'])
    @MulticastAddressNodeStep.setter
    def MulticastAddressNodeStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MulticastAddressNodeStep'], value)

    @property
    def MulticastIpv4Count(self):
        """
        Returns
        -------
        - number: The number of Multicast IPv4 addresses.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MulticastIpv4Count'])
    @MulticastIpv4Count.setter
    def MulticastIpv4Count(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MulticastIpv4Count'], value)

    @property
    def MulticastIpv4Step(self):
        """
        Returns
        -------
        - str: The incremental value of Multicast IPv4 address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['MulticastIpv4Step'])
    @MulticastIpv4Step.setter
    def MulticastIpv4Step(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MulticastIpv4Step'], value)

    @property
    def NoOfUnicastScrIpv4sPerMulicastIpv4(self):
        """
        Returns
        -------
        - number: The number of Unicast Source for each Multicast IPv4 address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfUnicastScrIpv4sPerMulicastIpv4'])
    @NoOfUnicastScrIpv4sPerMulicastIpv4.setter
    def NoOfUnicastScrIpv4sPerMulicastIpv4(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfUnicastScrIpv4sPerMulicastIpv4'], value)

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
    def StartMulticastIpv4(self):
        """
        Returns
        -------
        - str: The IP address format of the starting Multicast IPv4 address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartMulticastIpv4'])
    @StartMulticastIpv4.setter
    def StartMulticastIpv4(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartMulticastIpv4'], value)

    @property
    def StartUnicastSourceIpv4(self):
        """
        Returns
        -------
        - str: The IPv4 address format of the starting Unicast Source IPv4.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartUnicastSourceIpv4'])
    @StartUnicastSourceIpv4.setter
    def StartUnicastSourceIpv4(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartUnicastSourceIpv4'], value)

    @property
    def UnicastAddressNodeStep(self):
        """
        Returns
        -------
        - str: The Unicast IPv4 address that configures the increment across the Network Range simulated RBridges.
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
        - number: The VLAN ID of the enabled Multicast IPv4 Range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanId'])
    @VlanId.setter
    def VlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanId'], value)

    def update(self, IncludeIpv4Groups=None, InterGroupUnicastIpv4Increment=None, IntraGroupUnicastIpv4Increment=None, MulticastAddressNodeStep=None, MulticastIpv4Count=None, MulticastIpv4Step=None, NoOfUnicastScrIpv4sPerMulicastIpv4=None, SourceGroupMapping=None, StartMulticastIpv4=None, StartUnicastSourceIpv4=None, UnicastAddressNodeStep=None, VlanId=None):
        """Updates dceNodeIpv4Groups resource on the server.

        Args
        ----
        - IncludeIpv4Groups (bool): If true, includes IPv4 groups for this Network Range.
        - InterGroupUnicastIpv4Increment (str): The IPv4 address format of the Unicast IPv4 between one or more node groups.
        - IntraGroupUnicastIpv4Increment (str): The IPv4 address format of the Unicast MAC within a node group.
        - MulticastAddressNodeStep (str): The Multicast IPv4 address that configures the increment across the Network Range simulated RBridges.
        - MulticastIpv4Count (number): The number of Multicast IPv4 addresses.
        - MulticastIpv4Step (str): The incremental value of Multicast IPv4 address.
        - NoOfUnicastScrIpv4sPerMulicastIpv4 (number): The number of Unicast Source for each Multicast IPv4 address.
        - SourceGroupMapping (str(fullyMeshed | oneToOne | manualMapping)): The Source Group mapping type.
        - StartMulticastIpv4 (str): The IP address format of the starting Multicast IPv4 address.
        - StartUnicastSourceIpv4 (str): The IPv4 address format of the starting Unicast Source IPv4.
        - UnicastAddressNodeStep (str): The Unicast IPv4 address that configures the increment across the Network Range simulated RBridges.
        - VlanId (number): The VLAN ID of the enabled Multicast IPv4 Range.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, IncludeIpv4Groups=None, InterGroupUnicastIpv4Increment=None, IntraGroupUnicastIpv4Increment=None, MulticastAddressNodeStep=None, MulticastIpv4Count=None, MulticastIpv4Step=None, NoOfUnicastScrIpv4sPerMulicastIpv4=None, SourceGroupMapping=None, StartMulticastIpv4=None, StartUnicastSourceIpv4=None, UnicastAddressNodeStep=None, VlanId=None):
        """Adds a new dceNodeIpv4Groups resource on the server and adds it to the container.

        Args
        ----
        - IncludeIpv4Groups (bool): If true, includes IPv4 groups for this Network Range.
        - InterGroupUnicastIpv4Increment (str): The IPv4 address format of the Unicast IPv4 between one or more node groups.
        - IntraGroupUnicastIpv4Increment (str): The IPv4 address format of the Unicast MAC within a node group.
        - MulticastAddressNodeStep (str): The Multicast IPv4 address that configures the increment across the Network Range simulated RBridges.
        - MulticastIpv4Count (number): The number of Multicast IPv4 addresses.
        - MulticastIpv4Step (str): The incremental value of Multicast IPv4 address.
        - NoOfUnicastScrIpv4sPerMulicastIpv4 (number): The number of Unicast Source for each Multicast IPv4 address.
        - SourceGroupMapping (str(fullyMeshed | oneToOne | manualMapping)): The Source Group mapping type.
        - StartMulticastIpv4 (str): The IP address format of the starting Multicast IPv4 address.
        - StartUnicastSourceIpv4 (str): The IPv4 address format of the starting Unicast Source IPv4.
        - UnicastAddressNodeStep (str): The Unicast IPv4 address that configures the increment across the Network Range simulated RBridges.
        - VlanId (number): The VLAN ID of the enabled Multicast IPv4 Range.

        Returns
        -------
        - self: This instance with all currently retrieved dceNodeIpv4Groups resources using find and the newly added dceNodeIpv4Groups resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained dceNodeIpv4Groups resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, IncludeIpv4Groups=None, InterGroupUnicastIpv4Increment=None, IntraGroupUnicastIpv4Increment=None, MulticastAddressNodeStep=None, MulticastIpv4Count=None, MulticastIpv4Step=None, NoOfUnicastScrIpv4sPerMulicastIpv4=None, SourceGroupMapping=None, StartMulticastIpv4=None, StartUnicastSourceIpv4=None, UnicastAddressNodeStep=None, VlanId=None):
        """Finds and retrieves dceNodeIpv4Groups resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dceNodeIpv4Groups resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dceNodeIpv4Groups resources from the server.

        Args
        ----
        - IncludeIpv4Groups (bool): If true, includes IPv4 groups for this Network Range.
        - InterGroupUnicastIpv4Increment (str): The IPv4 address format of the Unicast IPv4 between one or more node groups.
        - IntraGroupUnicastIpv4Increment (str): The IPv4 address format of the Unicast MAC within a node group.
        - MulticastAddressNodeStep (str): The Multicast IPv4 address that configures the increment across the Network Range simulated RBridges.
        - MulticastIpv4Count (number): The number of Multicast IPv4 addresses.
        - MulticastIpv4Step (str): The incremental value of Multicast IPv4 address.
        - NoOfUnicastScrIpv4sPerMulicastIpv4 (number): The number of Unicast Source for each Multicast IPv4 address.
        - SourceGroupMapping (str(fullyMeshed | oneToOne | manualMapping)): The Source Group mapping type.
        - StartMulticastIpv4 (str): The IP address format of the starting Multicast IPv4 address.
        - StartUnicastSourceIpv4 (str): The IPv4 address format of the starting Unicast Source IPv4.
        - UnicastAddressNodeStep (str): The Unicast IPv4 address that configures the increment across the Network Range simulated RBridges.
        - VlanId (number): The VLAN ID of the enabled Multicast IPv4 Range.

        Returns
        -------
        - self: This instance with matching dceNodeIpv4Groups resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dceNodeIpv4Groups data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dceNodeIpv4Groups resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
