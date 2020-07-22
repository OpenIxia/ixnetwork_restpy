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


class Atm(Base):
    """This object holds the list  of statically-configured ATM Permanent Virtual Circuit (PVC) links for the port.
    The Atm class encapsulates a list of atm resources that are managed by the user.
    A list of resources can be retrieved from the server using the Atm.find() method.
    The list can be managed by using the Atm.add() and Atm.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'atm'
    _SDM_ATT_MAP = {
        'AtmEncapsulation': 'atmEncapsulation',
        'Count': 'count',
        'Enabled': 'enabled',
        'IncrementVci': 'incrementVci',
        'IncrementVpi': 'incrementVpi',
        'Name': 'name',
        'TrafficGroupId': 'trafficGroupId',
        'Vci': 'vci',
        'Vpi': 'vpi',
    }

    def __init__(self, parent):
        super(Atm, self).__init__(parent)

    @property
    def AtmEncapsulation(self):
        """
        Returns
        -------
        - str(llcRoutedSnap | llcBridged802p3WithFcs | llcBridged802p3WithOutFcs | ppp | vcMultiplexedPpp | vcMultiRouted | vcMultiBridged802p3WithFcs | vcMultiBridged802p3WithOutFcs): The type of ATM encapsulation to use for this ATM Name.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AtmEncapsulation'])
    @AtmEncapsulation.setter
    def AtmEncapsulation(self, value):
        self._set_attribute(self._SDM_ATT_MAP['AtmEncapsulation'], value)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: The total number of VPI/VCI pairs to create.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])
    @Count.setter
    def Count(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Count'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables this ATM VPI/VCI entry.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def IncrementVci(self):
        """
        Returns
        -------
        - number: Creates multiple VCIs. Each additional VCI will be incremented by 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrementVci'])
    @IncrementVci.setter
    def IncrementVci(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncrementVci'], value)

    @property
    def IncrementVpi(self):
        """
        Returns
        -------
        - number: Creates multiple VPIs. Each additional VPI will be incremented by 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrementVpi'])
    @IncrementVpi.setter
    def IncrementVpi(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncrementVpi'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: The identifier associated with this ATM VPI/VCI entry.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def TrafficGroupId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['TrafficGroupId'])
    @TrafficGroupId.setter
    def TrafficGroupId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['TrafficGroupId'], value)

    @property
    def Vci(self):
        """
        Returns
        -------
        - number: The value for the first ATM Virtual Circuit Identifier (VCI). The VCI value is used with a VPI value - a VPI/VCI pair - to identify a specific ATM link.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Vci'])
    @Vci.setter
    def Vci(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Vci'], value)

    @property
    def Vpi(self):
        """
        Returns
        -------
        - number: The value for the first ATM Virtual Port Identifier (VPI). The VPI value is used with a VCI value - a VPI/VCI pair - to identify a specific ATM virtual link.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Vpi'])
    @Vpi.setter
    def Vpi(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Vpi'], value)

    def update(self, AtmEncapsulation=None, Count=None, Enabled=None, IncrementVci=None, IncrementVpi=None, Name=None, TrafficGroupId=None, Vci=None, Vpi=None):
        """Updates atm resource on the server.

        Args
        ----
        - AtmEncapsulation (str(llcRoutedSnap | llcBridged802p3WithFcs | llcBridged802p3WithOutFcs | ppp | vcMultiplexedPpp | vcMultiRouted | vcMultiBridged802p3WithFcs | vcMultiBridged802p3WithOutFcs)): The type of ATM encapsulation to use for this ATM Name.
        - Count (number): The total number of VPI/VCI pairs to create.
        - Enabled (bool): Enables this ATM VPI/VCI entry.
        - IncrementVci (number): Creates multiple VCIs. Each additional VCI will be incremented by 1.
        - IncrementVpi (number): Creates multiple VPIs. Each additional VPI will be incremented by 1.
        - Name (str): The identifier associated with this ATM VPI/VCI entry.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        - Vci (number): The value for the first ATM Virtual Circuit Identifier (VCI). The VCI value is used with a VPI value - a VPI/VCI pair - to identify a specific ATM link.
        - Vpi (number): The value for the first ATM Virtual Port Identifier (VPI). The VPI value is used with a VCI value - a VPI/VCI pair - to identify a specific ATM virtual link.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AtmEncapsulation=None, Count=None, Enabled=None, IncrementVci=None, IncrementVpi=None, Name=None, TrafficGroupId=None, Vci=None, Vpi=None):
        """Adds a new atm resource on the server and adds it to the container.

        Args
        ----
        - AtmEncapsulation (str(llcRoutedSnap | llcBridged802p3WithFcs | llcBridged802p3WithOutFcs | ppp | vcMultiplexedPpp | vcMultiRouted | vcMultiBridged802p3WithFcs | vcMultiBridged802p3WithOutFcs)): The type of ATM encapsulation to use for this ATM Name.
        - Count (number): The total number of VPI/VCI pairs to create.
        - Enabled (bool): Enables this ATM VPI/VCI entry.
        - IncrementVci (number): Creates multiple VCIs. Each additional VCI will be incremented by 1.
        - IncrementVpi (number): Creates multiple VPIs. Each additional VPI will be incremented by 1.
        - Name (str): The identifier associated with this ATM VPI/VCI entry.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        - Vci (number): The value for the first ATM Virtual Circuit Identifier (VCI). The VCI value is used with a VPI value - a VPI/VCI pair - to identify a specific ATM link.
        - Vpi (number): The value for the first ATM Virtual Port Identifier (VPI). The VPI value is used with a VCI value - a VPI/VCI pair - to identify a specific ATM virtual link.

        Returns
        -------
        - self: This instance with all currently retrieved atm resources using find and the newly added atm resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained atm resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AtmEncapsulation=None, Count=None, Enabled=None, IncrementVci=None, IncrementVpi=None, Name=None, TrafficGroupId=None, Vci=None, Vpi=None):
        """Finds and retrieves atm resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve atm resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all atm resources from the server.

        Args
        ----
        - AtmEncapsulation (str(llcRoutedSnap | llcBridged802p3WithFcs | llcBridged802p3WithOutFcs | ppp | vcMultiplexedPpp | vcMultiRouted | vcMultiBridged802p3WithFcs | vcMultiBridged802p3WithOutFcs)): The type of ATM encapsulation to use for this ATM Name.
        - Count (number): The total number of VPI/VCI pairs to create.
        - Enabled (bool): Enables this ATM VPI/VCI entry.
        - IncrementVci (number): Creates multiple VCIs. Each additional VCI will be incremented by 1.
        - IncrementVpi (number): Creates multiple VPIs. Each additional VPI will be incremented by 1.
        - Name (str): The identifier associated with this ATM VPI/VCI entry.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.
        - Vci (number): The value for the first ATM Virtual Circuit Identifier (VCI). The VCI value is used with a VPI value - a VPI/VCI pair - to identify a specific ATM link.
        - Vpi (number): The value for the first ATM Virtual Port Identifier (VPI). The VPI value is used with a VCI value - a VPI/VCI pair - to identify a specific ATM virtual link.

        Returns
        -------
        - self: This instance with matching atm resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of atm data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the atm resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
