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


class CustomTopologyMulticastIpv6GroupRange(Base):
    """NOT DEFINED
    The CustomTopologyMulticastIpv6GroupRange class encapsulates a list of customTopologyMulticastIpv6GroupRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the CustomTopologyMulticastIpv6GroupRange.find() method.
    The list can be managed by using the CustomTopologyMulticastIpv6GroupRange.add() and CustomTopologyMulticastIpv6GroupRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'customTopologyMulticastIpv6GroupRange'
    _SDM_ATT_MAP = {
        'IncludeIpv6Groups': 'includeIpv6Groups',
        'IntergroupUnicastIpv6Increment': 'intergroupUnicastIpv6Increment',
        'IntraGroupUnicastIpv6Increment': 'intraGroupUnicastIpv6Increment',
        'MulticastAddressNodeStep': 'multicastAddressNodeStep',
        'MulticastIpv6Count': 'multicastIpv6Count',
        'MulticastIpv6Step': 'multicastIpv6Step',
        'NumberOfUnicastSourceIpv6MacsPerMulticastIpv6': 'numberOfUnicastSourceIpv6MacsPerMulticastIpv6',
        'SourceGroupMapping': 'sourceGroupMapping',
        'StartMulticastIpv6': 'startMulticastIpv6',
        'StartUnicastSourceIpv6': 'startUnicastSourceIpv6',
        'UnicastAddressNodeStep': 'unicastAddressNodeStep',
        'VlanId': 'vlanId',
    }

    def __init__(self, parent):
        super(CustomTopologyMulticastIpv6GroupRange, self).__init__(parent)

    @property
    def IncludeIpv6Groups(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeIpv6Groups'])
    @IncludeIpv6Groups.setter
    def IncludeIpv6Groups(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeIpv6Groups'], value)

    @property
    def IntergroupUnicastIpv6Increment(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['IntergroupUnicastIpv6Increment'])
    @IntergroupUnicastIpv6Increment.setter
    def IntergroupUnicastIpv6Increment(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IntergroupUnicastIpv6Increment'], value)

    @property
    def IntraGroupUnicastIpv6Increment(self):
        """
        Returns
        -------
        - str: NOT DEFINED
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
        - str: NOT DEFINED
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
        - number: NOT DEFINED
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
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MulticastIpv6Step'])
    @MulticastIpv6Step.setter
    def MulticastIpv6Step(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MulticastIpv6Step'], value)

    @property
    def NumberOfUnicastSourceIpv6MacsPerMulticastIpv6(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfUnicastSourceIpv6MacsPerMulticastIpv6'])
    @NumberOfUnicastSourceIpv6MacsPerMulticastIpv6.setter
    def NumberOfUnicastSourceIpv6MacsPerMulticastIpv6(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfUnicastSourceIpv6MacsPerMulticastIpv6'], value)

    @property
    def SourceGroupMapping(self):
        """
        Returns
        -------
        - str(fully-Meshed | one-To-One | manual-Mapping): NOT DEFINED
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
        - str: NOT DEFINED
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
        - str: NOT DEFINED
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
        - str: NOT DEFINED
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
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanId'])
    @VlanId.setter
    def VlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanId'], value)

    def update(self, IncludeIpv6Groups=None, IntergroupUnicastIpv6Increment=None, IntraGroupUnicastIpv6Increment=None, MulticastAddressNodeStep=None, MulticastIpv6Count=None, MulticastIpv6Step=None, NumberOfUnicastSourceIpv6MacsPerMulticastIpv6=None, SourceGroupMapping=None, StartMulticastIpv6=None, StartUnicastSourceIpv6=None, UnicastAddressNodeStep=None, VlanId=None):
        """Updates customTopologyMulticastIpv6GroupRange resource on the server.

        Args
        ----
        - IncludeIpv6Groups (bool): NOT DEFINED
        - IntergroupUnicastIpv6Increment (str): NOT DEFINED
        - IntraGroupUnicastIpv6Increment (str): NOT DEFINED
        - MulticastAddressNodeStep (str): NOT DEFINED
        - MulticastIpv6Count (number): NOT DEFINED
        - MulticastIpv6Step (str): NOT DEFINED
        - NumberOfUnicastSourceIpv6MacsPerMulticastIpv6 (number): NOT DEFINED
        - SourceGroupMapping (str(fully-Meshed | one-To-One | manual-Mapping)): NOT DEFINED
        - StartMulticastIpv6 (str): NOT DEFINED
        - StartUnicastSourceIpv6 (str): NOT DEFINED
        - UnicastAddressNodeStep (str): NOT DEFINED
        - VlanId (number): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, IncludeIpv6Groups=None, IntergroupUnicastIpv6Increment=None, IntraGroupUnicastIpv6Increment=None, MulticastAddressNodeStep=None, MulticastIpv6Count=None, MulticastIpv6Step=None, NumberOfUnicastSourceIpv6MacsPerMulticastIpv6=None, SourceGroupMapping=None, StartMulticastIpv6=None, StartUnicastSourceIpv6=None, UnicastAddressNodeStep=None, VlanId=None):
        """Adds a new customTopologyMulticastIpv6GroupRange resource on the server and adds it to the container.

        Args
        ----
        - IncludeIpv6Groups (bool): NOT DEFINED
        - IntergroupUnicastIpv6Increment (str): NOT DEFINED
        - IntraGroupUnicastIpv6Increment (str): NOT DEFINED
        - MulticastAddressNodeStep (str): NOT DEFINED
        - MulticastIpv6Count (number): NOT DEFINED
        - MulticastIpv6Step (str): NOT DEFINED
        - NumberOfUnicastSourceIpv6MacsPerMulticastIpv6 (number): NOT DEFINED
        - SourceGroupMapping (str(fully-Meshed | one-To-One | manual-Mapping)): NOT DEFINED
        - StartMulticastIpv6 (str): NOT DEFINED
        - StartUnicastSourceIpv6 (str): NOT DEFINED
        - UnicastAddressNodeStep (str): NOT DEFINED
        - VlanId (number): NOT DEFINED

        Returns
        -------
        - self: This instance with all currently retrieved customTopologyMulticastIpv6GroupRange resources using find and the newly added customTopologyMulticastIpv6GroupRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained customTopologyMulticastIpv6GroupRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, IncludeIpv6Groups=None, IntergroupUnicastIpv6Increment=None, IntraGroupUnicastIpv6Increment=None, MulticastAddressNodeStep=None, MulticastIpv6Count=None, MulticastIpv6Step=None, NumberOfUnicastSourceIpv6MacsPerMulticastIpv6=None, SourceGroupMapping=None, StartMulticastIpv6=None, StartUnicastSourceIpv6=None, UnicastAddressNodeStep=None, VlanId=None):
        """Finds and retrieves customTopologyMulticastIpv6GroupRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve customTopologyMulticastIpv6GroupRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all customTopologyMulticastIpv6GroupRange resources from the server.

        Args
        ----
        - IncludeIpv6Groups (bool): NOT DEFINED
        - IntergroupUnicastIpv6Increment (str): NOT DEFINED
        - IntraGroupUnicastIpv6Increment (str): NOT DEFINED
        - MulticastAddressNodeStep (str): NOT DEFINED
        - MulticastIpv6Count (number): NOT DEFINED
        - MulticastIpv6Step (str): NOT DEFINED
        - NumberOfUnicastSourceIpv6MacsPerMulticastIpv6 (number): NOT DEFINED
        - SourceGroupMapping (str(fully-Meshed | one-To-One | manual-Mapping)): NOT DEFINED
        - StartMulticastIpv6 (str): NOT DEFINED
        - StartUnicastSourceIpv6 (str): NOT DEFINED
        - UnicastAddressNodeStep (str): NOT DEFINED
        - VlanId (number): NOT DEFINED

        Returns
        -------
        - self: This instance with matching customTopologyMulticastIpv6GroupRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of customTopologyMulticastIpv6GroupRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the customTopologyMulticastIpv6GroupRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
