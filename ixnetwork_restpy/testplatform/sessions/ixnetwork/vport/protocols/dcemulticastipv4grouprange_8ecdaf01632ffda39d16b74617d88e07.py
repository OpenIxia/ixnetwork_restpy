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


class DceMulticastIpv4GroupRange(Base):
    """Sets the Multicast IPv4 Group Range for the DCE ISIS router.
    The DceMulticastIpv4GroupRange class encapsulates a list of dceMulticastIpv4GroupRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the DceMulticastIpv4GroupRange.find() method.
    The list can be managed by using the DceMulticastIpv4GroupRange.add() and DceMulticastIpv4GroupRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dceMulticastIpv4GroupRange'
    _SDM_ATT_MAP = {
        'Enabled': 'enabled',
        'InterGroupUnicastIpv4Increment': 'interGroupUnicastIpv4Increment',
        'IntraGroupUnicastIpv4Increment': 'intraGroupUnicastIpv4Increment',
        'MulticastIpv4Count': 'multicastIpv4Count',
        'MulticastIpv4Step': 'multicastIpv4Step',
        'SourceGroupMapping': 'sourceGroupMapping',
        'StartMulticastIpv4': 'startMulticastIpv4',
        'StartUnicastSourceIpv4': 'startUnicastSourceIpv4',
        'Topology': 'topology',
        'UnicastSourcesPerMulticastIpv4': 'unicastSourcesPerMulticastIpv4',
        'VlanId': 'vlanId',
    }

    def __init__(self, parent):
        super(DceMulticastIpv4GroupRange, self).__init__(parent)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, enables the Multicast IPv4 Group Range for a particular DCE ISIS route range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def InterGroupUnicastIpv4Increment(self):
        """
        Returns
        -------
        - str: The IPv4 address format of the Unicast IPv4 between one or more node groups. (Default = 00 00 00 00 00)
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
        - str: The IPv4 address format of the Unicast IPv4 within a node group. (default = 0.0.0.1)
        """
        return self._get_attribute(self._SDM_ATT_MAP['IntraGroupUnicastIpv4Increment'])
    @IntraGroupUnicastIpv4Increment.setter
    def IntraGroupUnicastIpv4Increment(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IntraGroupUnicastIpv4Increment'], value)

    @property
    def MulticastIpv4Count(self):
        """
        Returns
        -------
        - number: The number of Multicast IPv4 addresses. This field takes unsigned integer value ranging from 1 to UINT_MAX. (default = 1)
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
        - str: The incremental value of Multicast IPv4 address. (default = 0.0.0.1)
        """
        return self._get_attribute(self._SDM_ATT_MAP['MulticastIpv4Step'])
    @MulticastIpv4Step.setter
    def MulticastIpv4Step(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MulticastIpv4Step'], value)

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
        - str: The IP address format of the starting Multicast IPv4 address. (default = 224.0.0.0)
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
        - str: The IPv4 address format of the starting Unicast Source IPv4. (default = 0.0.0.0)
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartUnicastSourceIpv4'])
    @StartUnicastSourceIpv4.setter
    def StartUnicastSourceIpv4(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartUnicastSourceIpv4'], value)

    @property
    def Topology(self):
        """
        Returns
        -------
        - number: The topology identifier to which the corresponding IpV4 belongs.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Topology'])
    @Topology.setter
    def Topology(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Topology'], value)

    @property
    def UnicastSourcesPerMulticastIpv4(self):
        """
        Returns
        -------
        - number: The number of Unicast Source for each Multicast IPv4 address. (default = 1)
        """
        return self._get_attribute(self._SDM_ATT_MAP['UnicastSourcesPerMulticastIpv4'])
    @UnicastSourcesPerMulticastIpv4.setter
    def UnicastSourcesPerMulticastIpv4(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UnicastSourcesPerMulticastIpv4'], value)

    @property
    def VlanId(self):
        """
        Returns
        -------
        - number: The VLAN ID of the enabled Multicast IPv4 Group Range. (default =1)
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanId'])
    @VlanId.setter
    def VlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanId'], value)

    def update(self, Enabled=None, InterGroupUnicastIpv4Increment=None, IntraGroupUnicastIpv4Increment=None, MulticastIpv4Count=None, MulticastIpv4Step=None, SourceGroupMapping=None, StartMulticastIpv4=None, StartUnicastSourceIpv4=None, Topology=None, UnicastSourcesPerMulticastIpv4=None, VlanId=None):
        """Updates dceMulticastIpv4GroupRange resource on the server.

        Args
        ----
        - Enabled (bool): If true, enables the Multicast IPv4 Group Range for a particular DCE ISIS route range.
        - InterGroupUnicastIpv4Increment (str): The IPv4 address format of the Unicast IPv4 between one or more node groups. (Default = 00 00 00 00 00)
        - IntraGroupUnicastIpv4Increment (str): The IPv4 address format of the Unicast IPv4 within a node group. (default = 0.0.0.1)
        - MulticastIpv4Count (number): The number of Multicast IPv4 addresses. This field takes unsigned integer value ranging from 1 to UINT_MAX. (default = 1)
        - MulticastIpv4Step (str): The incremental value of Multicast IPv4 address. (default = 0.0.0.1)
        - SourceGroupMapping (str(fullyMeshed | oneToOne | manualMapping)): The Source Group mapping type.
        - StartMulticastIpv4 (str): The IP address format of the starting Multicast IPv4 address. (default = 224.0.0.0)
        - StartUnicastSourceIpv4 (str): The IPv4 address format of the starting Unicast Source IPv4. (default = 0.0.0.0)
        - Topology (number): The topology identifier to which the corresponding IpV4 belongs.
        - UnicastSourcesPerMulticastIpv4 (number): The number of Unicast Source for each Multicast IPv4 address. (default = 1)
        - VlanId (number): The VLAN ID of the enabled Multicast IPv4 Group Range. (default =1)

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Enabled=None, InterGroupUnicastIpv4Increment=None, IntraGroupUnicastIpv4Increment=None, MulticastIpv4Count=None, MulticastIpv4Step=None, SourceGroupMapping=None, StartMulticastIpv4=None, StartUnicastSourceIpv4=None, Topology=None, UnicastSourcesPerMulticastIpv4=None, VlanId=None):
        """Adds a new dceMulticastIpv4GroupRange resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): If true, enables the Multicast IPv4 Group Range for a particular DCE ISIS route range.
        - InterGroupUnicastIpv4Increment (str): The IPv4 address format of the Unicast IPv4 between one or more node groups. (Default = 00 00 00 00 00)
        - IntraGroupUnicastIpv4Increment (str): The IPv4 address format of the Unicast IPv4 within a node group. (default = 0.0.0.1)
        - MulticastIpv4Count (number): The number of Multicast IPv4 addresses. This field takes unsigned integer value ranging from 1 to UINT_MAX. (default = 1)
        - MulticastIpv4Step (str): The incremental value of Multicast IPv4 address. (default = 0.0.0.1)
        - SourceGroupMapping (str(fullyMeshed | oneToOne | manualMapping)): The Source Group mapping type.
        - StartMulticastIpv4 (str): The IP address format of the starting Multicast IPv4 address. (default = 224.0.0.0)
        - StartUnicastSourceIpv4 (str): The IPv4 address format of the starting Unicast Source IPv4. (default = 0.0.0.0)
        - Topology (number): The topology identifier to which the corresponding IpV4 belongs.
        - UnicastSourcesPerMulticastIpv4 (number): The number of Unicast Source for each Multicast IPv4 address. (default = 1)
        - VlanId (number): The VLAN ID of the enabled Multicast IPv4 Group Range. (default =1)

        Returns
        -------
        - self: This instance with all currently retrieved dceMulticastIpv4GroupRange resources using find and the newly added dceMulticastIpv4GroupRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained dceMulticastIpv4GroupRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, InterGroupUnicastIpv4Increment=None, IntraGroupUnicastIpv4Increment=None, MulticastIpv4Count=None, MulticastIpv4Step=None, SourceGroupMapping=None, StartMulticastIpv4=None, StartUnicastSourceIpv4=None, Topology=None, UnicastSourcesPerMulticastIpv4=None, VlanId=None):
        """Finds and retrieves dceMulticastIpv4GroupRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dceMulticastIpv4GroupRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dceMulticastIpv4GroupRange resources from the server.

        Args
        ----
        - Enabled (bool): If true, enables the Multicast IPv4 Group Range for a particular DCE ISIS route range.
        - InterGroupUnicastIpv4Increment (str): The IPv4 address format of the Unicast IPv4 between one or more node groups. (Default = 00 00 00 00 00)
        - IntraGroupUnicastIpv4Increment (str): The IPv4 address format of the Unicast IPv4 within a node group. (default = 0.0.0.1)
        - MulticastIpv4Count (number): The number of Multicast IPv4 addresses. This field takes unsigned integer value ranging from 1 to UINT_MAX. (default = 1)
        - MulticastIpv4Step (str): The incremental value of Multicast IPv4 address. (default = 0.0.0.1)
        - SourceGroupMapping (str(fullyMeshed | oneToOne | manualMapping)): The Source Group mapping type.
        - StartMulticastIpv4 (str): The IP address format of the starting Multicast IPv4 address. (default = 224.0.0.0)
        - StartUnicastSourceIpv4 (str): The IPv4 address format of the starting Unicast Source IPv4. (default = 0.0.0.0)
        - Topology (number): The topology identifier to which the corresponding IpV4 belongs.
        - UnicastSourcesPerMulticastIpv4 (number): The number of Unicast Source for each Multicast IPv4 address. (default = 1)
        - VlanId (number): The VLAN ID of the enabled Multicast IPv4 Group Range. (default =1)

        Returns
        -------
        - self: This instance with matching dceMulticastIpv4GroupRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dceMulticastIpv4GroupRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dceMulticastIpv4GroupRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
