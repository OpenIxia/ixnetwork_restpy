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


class CustomTopologyMulticastMacRange(Base):
    """NOT DEFINED
    The CustomTopologyMulticastMacRange class encapsulates a list of customTopologyMulticastMacRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the CustomTopologyMulticastMacRange.find() method.
    The list can be managed by using the CustomTopologyMulticastMacRange.add() and CustomTopologyMulticastMacRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'customTopologyMulticastMacRange'
    _SDM_ATT_MAP = {
        'IncludeMacGroup': 'includeMacGroup',
        'IntraGroupUnicastMacIncrement': 'intraGroupUnicastMacIncrement',
        'MulticastAddressNodeStep': 'multicastAddressNodeStep',
        'MulticastMacCount': 'multicastMacCount',
        'MulticastMacStep': 'multicastMacStep',
        'NumberOfUnicastSourceMacsPerMulticast': 'numberOfUnicastSourceMacsPerMulticast',
        'SourceGroupMapping': 'sourceGroupMapping',
        'StartMulticastMac': 'startMulticastMac',
        'StartUnicastSourceMac': 'startUnicastSourceMac',
        'UnicastAddressNodeStep': 'unicastAddressNodeStep',
        'VlanId': 'vlanId',
    }

    def __init__(self, parent):
        super(CustomTopologyMulticastMacRange, self).__init__(parent)

    @property
    def IncludeMacGroup(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeMacGroup'])
    @IncludeMacGroup.setter
    def IncludeMacGroup(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeMacGroup'], value)

    @property
    def IntraGroupUnicastMacIncrement(self):
        """
        Returns
        -------
        - str: NOT DEFINED
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
        - str: NOT DEFINED
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
        - number: NOT DEFINED
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
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MulticastMacStep'])
    @MulticastMacStep.setter
    def MulticastMacStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MulticastMacStep'], value)

    @property
    def NumberOfUnicastSourceMacsPerMulticast(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfUnicastSourceMacsPerMulticast'])
    @NumberOfUnicastSourceMacsPerMulticast.setter
    def NumberOfUnicastSourceMacsPerMulticast(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfUnicastSourceMacsPerMulticast'], value)

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
    def StartMulticastMac(self):
        """
        Returns
        -------
        - str: NOT DEFINED
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
        - str: NOT DEFINED
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

    def update(self, IncludeMacGroup=None, IntraGroupUnicastMacIncrement=None, MulticastAddressNodeStep=None, MulticastMacCount=None, MulticastMacStep=None, NumberOfUnicastSourceMacsPerMulticast=None, SourceGroupMapping=None, StartMulticastMac=None, StartUnicastSourceMac=None, UnicastAddressNodeStep=None, VlanId=None):
        """Updates customTopologyMulticastMacRange resource on the server.

        Args
        ----
        - IncludeMacGroup (bool): NOT DEFINED
        - IntraGroupUnicastMacIncrement (str): NOT DEFINED
        - MulticastAddressNodeStep (str): NOT DEFINED
        - MulticastMacCount (number): NOT DEFINED
        - MulticastMacStep (str): NOT DEFINED
        - NumberOfUnicastSourceMacsPerMulticast (number): NOT DEFINED
        - SourceGroupMapping (str(fully-Meshed | one-To-One | manual-Mapping)): NOT DEFINED
        - StartMulticastMac (str): NOT DEFINED
        - StartUnicastSourceMac (str): NOT DEFINED
        - UnicastAddressNodeStep (str): NOT DEFINED
        - VlanId (number): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, IncludeMacGroup=None, IntraGroupUnicastMacIncrement=None, MulticastAddressNodeStep=None, MulticastMacCount=None, MulticastMacStep=None, NumberOfUnicastSourceMacsPerMulticast=None, SourceGroupMapping=None, StartMulticastMac=None, StartUnicastSourceMac=None, UnicastAddressNodeStep=None, VlanId=None):
        """Adds a new customTopologyMulticastMacRange resource on the server and adds it to the container.

        Args
        ----
        - IncludeMacGroup (bool): NOT DEFINED
        - IntraGroupUnicastMacIncrement (str): NOT DEFINED
        - MulticastAddressNodeStep (str): NOT DEFINED
        - MulticastMacCount (number): NOT DEFINED
        - MulticastMacStep (str): NOT DEFINED
        - NumberOfUnicastSourceMacsPerMulticast (number): NOT DEFINED
        - SourceGroupMapping (str(fully-Meshed | one-To-One | manual-Mapping)): NOT DEFINED
        - StartMulticastMac (str): NOT DEFINED
        - StartUnicastSourceMac (str): NOT DEFINED
        - UnicastAddressNodeStep (str): NOT DEFINED
        - VlanId (number): NOT DEFINED

        Returns
        -------
        - self: This instance with all currently retrieved customTopologyMulticastMacRange resources using find and the newly added customTopologyMulticastMacRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained customTopologyMulticastMacRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, IncludeMacGroup=None, IntraGroupUnicastMacIncrement=None, MulticastAddressNodeStep=None, MulticastMacCount=None, MulticastMacStep=None, NumberOfUnicastSourceMacsPerMulticast=None, SourceGroupMapping=None, StartMulticastMac=None, StartUnicastSourceMac=None, UnicastAddressNodeStep=None, VlanId=None):
        """Finds and retrieves customTopologyMulticastMacRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve customTopologyMulticastMacRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all customTopologyMulticastMacRange resources from the server.

        Args
        ----
        - IncludeMacGroup (bool): NOT DEFINED
        - IntraGroupUnicastMacIncrement (str): NOT DEFINED
        - MulticastAddressNodeStep (str): NOT DEFINED
        - MulticastMacCount (number): NOT DEFINED
        - MulticastMacStep (str): NOT DEFINED
        - NumberOfUnicastSourceMacsPerMulticast (number): NOT DEFINED
        - SourceGroupMapping (str(fully-Meshed | one-To-One | manual-Mapping)): NOT DEFINED
        - StartMulticastMac (str): NOT DEFINED
        - StartUnicastSourceMac (str): NOT DEFINED
        - UnicastAddressNodeStep (str): NOT DEFINED
        - VlanId (number): NOT DEFINED

        Returns
        -------
        - self: This instance with matching customTopologyMulticastMacRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of customTopologyMulticastMacRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the customTopologyMulticastMacRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
