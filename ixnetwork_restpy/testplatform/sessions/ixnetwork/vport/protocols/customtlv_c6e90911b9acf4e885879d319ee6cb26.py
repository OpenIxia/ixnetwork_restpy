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


class CustomTlv(Base):
    """NOT DEFINED
    The CustomTlv class encapsulates a list of customTlv resources that are managed by the user.
    A list of resources can be retrieved from the server using the CustomTlv.find() method.
    The list can be managed by using the CustomTlv.add() and CustomTlv.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'customTlv'
    _SDM_ATT_MAP = {
        'Enabled': 'enabled',
        'IncludeInHello': 'includeInHello',
        'IncludeInLsp': 'includeInLsp',
        'IncludeInNetworkRange': 'includeInNetworkRange',
        'Length': 'length',
        'Type': 'type',
        'Value': 'value',
    }

    def __init__(self, parent):
        super(CustomTlv, self).__init__(parent)

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
    def IncludeInHello(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeInHello'])
    @IncludeInHello.setter
    def IncludeInHello(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeInHello'], value)

    @property
    def IncludeInLsp(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeInLsp'])
    @IncludeInLsp.setter
    def IncludeInLsp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeInLsp'], value)

    @property
    def IncludeInNetworkRange(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeInNetworkRange'])
    @IncludeInNetworkRange.setter
    def IncludeInNetworkRange(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeInNetworkRange'], value)

    @property
    def Length(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Length'])
    @Length.setter
    def Length(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Length'], value)

    @property
    def Type(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Type'])
    @Type.setter
    def Type(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Type'], value)

    @property
    def Value(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['Value'])
    @Value.setter
    def Value(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Value'], value)

    def update(self, Enabled=None, IncludeInHello=None, IncludeInLsp=None, IncludeInNetworkRange=None, Length=None, Type=None, Value=None):
        """Updates customTlv resource on the server.

        Args
        ----
        - Enabled (bool): NOT DEFINED
        - IncludeInHello (bool): NOT DEFINED
        - IncludeInLsp (bool): NOT DEFINED
        - IncludeInNetworkRange (bool): NOT DEFINED
        - Length (number): NOT DEFINED
        - Type (number): NOT DEFINED
        - Value (str): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Enabled=None, IncludeInHello=None, IncludeInLsp=None, IncludeInNetworkRange=None, Length=None, Type=None, Value=None):
        """Adds a new customTlv resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): NOT DEFINED
        - IncludeInHello (bool): NOT DEFINED
        - IncludeInLsp (bool): NOT DEFINED
        - IncludeInNetworkRange (bool): NOT DEFINED
        - Length (number): NOT DEFINED
        - Type (number): NOT DEFINED
        - Value (str): NOT DEFINED

        Returns
        -------
        - self: This instance with all currently retrieved customTlv resources using find and the newly added customTlv resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained customTlv resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, IncludeInHello=None, IncludeInLsp=None, IncludeInNetworkRange=None, Length=None, Type=None, Value=None):
        """Finds and retrieves customTlv resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve customTlv resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all customTlv resources from the server.

        Args
        ----
        - Enabled (bool): NOT DEFINED
        - IncludeInHello (bool): NOT DEFINED
        - IncludeInLsp (bool): NOT DEFINED
        - IncludeInNetworkRange (bool): NOT DEFINED
        - Length (number): NOT DEFINED
        - Type (number): NOT DEFINED
        - Value (str): NOT DEFINED

        Returns
        -------
        - self: This instance with matching customTlv resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of customTlv data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the customTlv resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
