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


class CustomTopologyMulticastIpv4GroupRange(Base):
    """NOT DEFINED
    The CustomTopologyMulticastIpv4GroupRange class encapsulates a list of customTopologyMulticastIpv4GroupRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the CustomTopologyMulticastIpv4GroupRange.find() method.
    The list can be managed by using the CustomTopologyMulticastIpv4GroupRange.add() and CustomTopologyMulticastIpv4GroupRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'customTopologyMulticastIpv4GroupRange'
    _SDM_ATT_MAP = {
        'IncludeIpv4Groups': 'includeIpv4Groups',
        'IntraGroupUnicastIpv4Increment': 'intraGroupUnicastIpv4Increment',
        'MulticastAddressNodeStep': 'multicastAddressNodeStep',
        'MulticastIpv4Count': 'multicastIpv4Count',
        'MulticastIpv4Step': 'multicastIpv4Step',
        'NoOfUcSrcIpv4MacsPerMcIpv4': 'noOfUcSrcIpv4MacsPerMcIpv4',
        'SourceGroupMapping': 'sourceGroupMapping',
        'StartMulticastIpv4': 'startMulticastIpv4',
        'StartUnicastSourceIpv4': 'startUnicastSourceIpv4',
        'UnicastAddressNodeStep': 'unicastAddressNodeStep',
        'VlanId': 'vlanId',
    }

    def __init__(self, parent):
        super(CustomTopologyMulticastIpv4GroupRange, self).__init__(parent)

    @property
    def IncludeIpv4Groups(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeIpv4Groups'])
    @IncludeIpv4Groups.setter
    def IncludeIpv4Groups(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeIpv4Groups'], value)

    @property
    def IntraGroupUnicastIpv4Increment(self):
        """
        Returns
        -------
        - str: NOT DEFINED
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
        - str: NOT DEFINED
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
        - number: NOT DEFINED
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
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MulticastIpv4Step'])
    @MulticastIpv4Step.setter
    def MulticastIpv4Step(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MulticastIpv4Step'], value)

    @property
    def NoOfUcSrcIpv4MacsPerMcIpv4(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfUcSrcIpv4MacsPerMcIpv4'])
    @NoOfUcSrcIpv4MacsPerMcIpv4.setter
    def NoOfUcSrcIpv4MacsPerMcIpv4(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfUcSrcIpv4MacsPerMcIpv4'], value)

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
    def StartMulticastIpv4(self):
        """
        Returns
        -------
        - str: NOT DEFINED
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
        - str: NOT DEFINED
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

    def update(self, IncludeIpv4Groups=None, IntraGroupUnicastIpv4Increment=None, MulticastAddressNodeStep=None, MulticastIpv4Count=None, MulticastIpv4Step=None, NoOfUcSrcIpv4MacsPerMcIpv4=None, SourceGroupMapping=None, StartMulticastIpv4=None, StartUnicastSourceIpv4=None, UnicastAddressNodeStep=None, VlanId=None):
        """Updates customTopologyMulticastIpv4GroupRange resource on the server.

        Args
        ----
        - IncludeIpv4Groups (bool): NOT DEFINED
        - IntraGroupUnicastIpv4Increment (str): NOT DEFINED
        - MulticastAddressNodeStep (str): NOT DEFINED
        - MulticastIpv4Count (number): NOT DEFINED
        - MulticastIpv4Step (str): NOT DEFINED
        - NoOfUcSrcIpv4MacsPerMcIpv4 (number): NOT DEFINED
        - SourceGroupMapping (str(fully-Meshed | one-To-One | manual-Mapping)): NOT DEFINED
        - StartMulticastIpv4 (str): NOT DEFINED
        - StartUnicastSourceIpv4 (str): NOT DEFINED
        - UnicastAddressNodeStep (str): NOT DEFINED
        - VlanId (number): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, IncludeIpv4Groups=None, IntraGroupUnicastIpv4Increment=None, MulticastAddressNodeStep=None, MulticastIpv4Count=None, MulticastIpv4Step=None, NoOfUcSrcIpv4MacsPerMcIpv4=None, SourceGroupMapping=None, StartMulticastIpv4=None, StartUnicastSourceIpv4=None, UnicastAddressNodeStep=None, VlanId=None):
        """Adds a new customTopologyMulticastIpv4GroupRange resource on the server and adds it to the container.

        Args
        ----
        - IncludeIpv4Groups (bool): NOT DEFINED
        - IntraGroupUnicastIpv4Increment (str): NOT DEFINED
        - MulticastAddressNodeStep (str): NOT DEFINED
        - MulticastIpv4Count (number): NOT DEFINED
        - MulticastIpv4Step (str): NOT DEFINED
        - NoOfUcSrcIpv4MacsPerMcIpv4 (number): NOT DEFINED
        - SourceGroupMapping (str(fully-Meshed | one-To-One | manual-Mapping)): NOT DEFINED
        - StartMulticastIpv4 (str): NOT DEFINED
        - StartUnicastSourceIpv4 (str): NOT DEFINED
        - UnicastAddressNodeStep (str): NOT DEFINED
        - VlanId (number): NOT DEFINED

        Returns
        -------
        - self: This instance with all currently retrieved customTopologyMulticastIpv4GroupRange resources using find and the newly added customTopologyMulticastIpv4GroupRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained customTopologyMulticastIpv4GroupRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, IncludeIpv4Groups=None, IntraGroupUnicastIpv4Increment=None, MulticastAddressNodeStep=None, MulticastIpv4Count=None, MulticastIpv4Step=None, NoOfUcSrcIpv4MacsPerMcIpv4=None, SourceGroupMapping=None, StartMulticastIpv4=None, StartUnicastSourceIpv4=None, UnicastAddressNodeStep=None, VlanId=None):
        """Finds and retrieves customTopologyMulticastIpv4GroupRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve customTopologyMulticastIpv4GroupRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all customTopologyMulticastIpv4GroupRange resources from the server.

        Args
        ----
        - IncludeIpv4Groups (bool): NOT DEFINED
        - IntraGroupUnicastIpv4Increment (str): NOT DEFINED
        - MulticastAddressNodeStep (str): NOT DEFINED
        - MulticastIpv4Count (number): NOT DEFINED
        - MulticastIpv4Step (str): NOT DEFINED
        - NoOfUcSrcIpv4MacsPerMcIpv4 (number): NOT DEFINED
        - SourceGroupMapping (str(fully-Meshed | one-To-One | manual-Mapping)): NOT DEFINED
        - StartMulticastIpv4 (str): NOT DEFINED
        - StartUnicastSourceIpv4 (str): NOT DEFINED
        - UnicastAddressNodeStep (str): NOT DEFINED
        - VlanId (number): NOT DEFINED

        Returns
        -------
        - self: This instance with matching customTopologyMulticastIpv4GroupRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of customTopologyMulticastIpv4GroupRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the customTopologyMulticastIpv4GroupRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
