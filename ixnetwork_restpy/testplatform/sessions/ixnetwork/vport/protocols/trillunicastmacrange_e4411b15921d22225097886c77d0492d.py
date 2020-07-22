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


class TrillUnicastMacRange(Base):
    """The TRILL unicast MAC Range.
    The TrillUnicastMacRange class encapsulates a list of trillUnicastMacRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the TrillUnicastMacRange.find() method.
    The list can be managed by using the TrillUnicastMacRange.add() and TrillUnicastMacRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'trillUnicastMacRange'
    _SDM_ATT_MAP = {
        'Enabled': 'enabled',
        'StartUnicastMac': 'startUnicastMac',
        'Topology': 'topology',
        'UnicastMacCount': 'unicastMacCount',
        'UnicastMacStep': 'unicastMacStep',
        'VlanId': 'vlanId',
    }

    def __init__(self, parent):
        super(TrillUnicastMacRange, self).__init__(parent)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: If true, enables the use of TRILL unicast MAC range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def StartUnicastMac(self):
        """
        Returns
        -------
        - str: Starts unicast MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartUnicastMac'])
    @StartUnicastMac.setter
    def StartUnicastMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartUnicastMac'], value)

    @property
    def Topology(self):
        """
        Returns
        -------
        - number: Signifies the topology range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Topology'])

    @property
    def UnicastMacCount(self):
        """
        Returns
        -------
        - number: Signifies the count of unicast MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UnicastMacCount'])
    @UnicastMacCount.setter
    def UnicastMacCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UnicastMacCount'], value)

    @property
    def UnicastMacStep(self):
        """
        Returns
        -------
        - str: Signifies the step value of unicast MAC address.
        """
        return self._get_attribute(self._SDM_ATT_MAP['UnicastMacStep'])
    @UnicastMacStep.setter
    def UnicastMacStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['UnicastMacStep'], value)

    @property
    def VlanId(self):
        """
        Returns
        -------
        - number: Signifies VLAN identifier.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanId'])
    @VlanId.setter
    def VlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanId'], value)

    def update(self, Enabled=None, StartUnicastMac=None, UnicastMacCount=None, UnicastMacStep=None, VlanId=None):
        """Updates trillUnicastMacRange resource on the server.

        Args
        ----
        - Enabled (bool): If true, enables the use of TRILL unicast MAC range.
        - StartUnicastMac (str): Starts unicast MAC address.
        - UnicastMacCount (number): Signifies the count of unicast MAC address.
        - UnicastMacStep (str): Signifies the step value of unicast MAC address.
        - VlanId (number): Signifies VLAN identifier.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Enabled=None, StartUnicastMac=None, UnicastMacCount=None, UnicastMacStep=None, VlanId=None):
        """Adds a new trillUnicastMacRange resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): If true, enables the use of TRILL unicast MAC range.
        - StartUnicastMac (str): Starts unicast MAC address.
        - UnicastMacCount (number): Signifies the count of unicast MAC address.
        - UnicastMacStep (str): Signifies the step value of unicast MAC address.
        - VlanId (number): Signifies VLAN identifier.

        Returns
        -------
        - self: This instance with all currently retrieved trillUnicastMacRange resources using find and the newly added trillUnicastMacRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained trillUnicastMacRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, StartUnicastMac=None, Topology=None, UnicastMacCount=None, UnicastMacStep=None, VlanId=None):
        """Finds and retrieves trillUnicastMacRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve trillUnicastMacRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all trillUnicastMacRange resources from the server.

        Args
        ----
        - Enabled (bool): If true, enables the use of TRILL unicast MAC range.
        - StartUnicastMac (str): Starts unicast MAC address.
        - Topology (number): Signifies the topology range.
        - UnicastMacCount (number): Signifies the count of unicast MAC address.
        - UnicastMacStep (str): Signifies the step value of unicast MAC address.
        - VlanId (number): Signifies VLAN identifier.

        Returns
        -------
        - self: This instance with matching trillUnicastMacRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of trillUnicastMacRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the trillUnicastMacRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
