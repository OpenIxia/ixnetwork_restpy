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


class CustomTopologyUnicastMacRange(Base):
    """NOT DEFINED
    The CustomTopologyUnicastMacRange class encapsulates a list of customTopologyUnicastMacRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the CustomTopologyUnicastMacRange.find() method.
    The list can be managed by using the CustomTopologyUnicastMacRange.add() and CustomTopologyUnicastMacRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'customTopologyUnicastMacRange'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'Enabled': 'enabled',
        'InterNodeMacIncrement': 'interNodeMacIncrement',
        'MacIncrement': 'macIncrement',
        'StartMac': 'startMac',
        'StartVlanId': 'startVlanId',
    }

    def __init__(self, parent):
        super(CustomTopologyUnicastMacRange, self).__init__(parent)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: NOT DEFINED
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
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def InterNodeMacIncrement(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterNodeMacIncrement'])
    @InterNodeMacIncrement.setter
    def InterNodeMacIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterNodeMacIncrement'], value)

    @property
    def MacIncrement(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['MacIncrement'])
    @MacIncrement.setter
    def MacIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['MacIncrement'], value)

    @property
    def StartMac(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartMac'])
    @StartMac.setter
    def StartMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartMac'], value)

    @property
    def StartVlanId(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartVlanId'])
    @StartVlanId.setter
    def StartVlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartVlanId'], value)

    def update(self, Count=None, Enabled=None, InterNodeMacIncrement=None, MacIncrement=None, StartMac=None, StartVlanId=None):
        """Updates customTopologyUnicastMacRange resource on the server.

        Args
        ----
        - Count (number): NOT DEFINED
        - Enabled (bool): NOT DEFINED
        - InterNodeMacIncrement (str): NOT DEFINED
        - MacIncrement (str): NOT DEFINED
        - StartMac (str): NOT DEFINED
        - StartVlanId (number): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Count=None, Enabled=None, InterNodeMacIncrement=None, MacIncrement=None, StartMac=None, StartVlanId=None):
        """Adds a new customTopologyUnicastMacRange resource on the server and adds it to the container.

        Args
        ----
        - Count (number): NOT DEFINED
        - Enabled (bool): NOT DEFINED
        - InterNodeMacIncrement (str): NOT DEFINED
        - MacIncrement (str): NOT DEFINED
        - StartMac (str): NOT DEFINED
        - StartVlanId (number): NOT DEFINED

        Returns
        -------
        - self: This instance with all currently retrieved customTopologyUnicastMacRange resources using find and the newly added customTopologyUnicastMacRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained customTopologyUnicastMacRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Count=None, Enabled=None, InterNodeMacIncrement=None, MacIncrement=None, StartMac=None, StartVlanId=None):
        """Finds and retrieves customTopologyUnicastMacRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve customTopologyUnicastMacRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all customTopologyUnicastMacRange resources from the server.

        Args
        ----
        - Count (number): NOT DEFINED
        - Enabled (bool): NOT DEFINED
        - InterNodeMacIncrement (str): NOT DEFINED
        - MacIncrement (str): NOT DEFINED
        - StartMac (str): NOT DEFINED
        - StartVlanId (number): NOT DEFINED

        Returns
        -------
        - self: This instance with matching customTopologyUnicastMacRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of customTopologyUnicastMacRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the customTopologyUnicastMacRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
