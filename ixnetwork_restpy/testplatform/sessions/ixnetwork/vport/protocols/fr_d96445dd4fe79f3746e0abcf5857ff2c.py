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


class Fr(Base):
    """This object holds the list of statically-configured Frame Relay DLCIs for the port.
    The Fr class encapsulates a list of fr resources that are managed by the user.
    A list of resources can be retrieved from the server using the Fr.find() method.
    The list can be managed by using the Fr.add() and Fr.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'fr'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'Dlci': 'dlci',
        'EnableIncrement': 'enableIncrement',
        'Enabled': 'enabled',
        'TrafficGroupId': 'trafficGroupId',
    }

    def __init__(self, parent):
        super(Fr, self).__init__(parent)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: The total number of DLCIs to create for this range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])
    @Count.setter
    def Count(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Count'], value)

    @property
    def Dlci(self):
        """
        Returns
        -------
        - number: The Data Link Connection Identifier (DLCI) value.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Dlci'])
    @Dlci.setter
    def Dlci(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Dlci'], value)

    @property
    def EnableIncrement(self):
        """
        Returns
        -------
        - bool: Creates a range of DLCIs for this entry. Each additional DLCI value will be incremented by 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableIncrement'])
    @EnableIncrement.setter
    def EnableIncrement(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableIncrement'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Check this box to enable this Frame Relay (FR) DLCI entry.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

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

    def update(self, Count=None, Dlci=None, EnableIncrement=None, Enabled=None, TrafficGroupId=None):
        """Updates fr resource on the server.

        Args
        ----
        - Count (number): The total number of DLCIs to create for this range.
        - Dlci (number): The Data Link Connection Identifier (DLCI) value.
        - EnableIncrement (bool): Creates a range of DLCIs for this entry. Each additional DLCI value will be incremented by 1.
        - Enabled (bool): Check this box to enable this Frame Relay (FR) DLCI entry.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Count=None, Dlci=None, EnableIncrement=None, Enabled=None, TrafficGroupId=None):
        """Adds a new fr resource on the server and adds it to the container.

        Args
        ----
        - Count (number): The total number of DLCIs to create for this range.
        - Dlci (number): The Data Link Connection Identifier (DLCI) value.
        - EnableIncrement (bool): Creates a range of DLCIs for this entry. Each additional DLCI value will be incremented by 1.
        - Enabled (bool): Check this box to enable this Frame Relay (FR) DLCI entry.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.

        Returns
        -------
        - self: This instance with all currently retrieved fr resources using find and the newly added fr resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained fr resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Count=None, Dlci=None, EnableIncrement=None, Enabled=None, TrafficGroupId=None):
        """Finds and retrieves fr resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve fr resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all fr resources from the server.

        Args
        ----
        - Count (number): The total number of DLCIs to create for this range.
        - Dlci (number): The Data Link Connection Identifier (DLCI) value.
        - EnableIncrement (bool): Creates a range of DLCIs for this entry. Each additional DLCI value will be incremented by 1.
        - Enabled (bool): Check this box to enable this Frame Relay (FR) DLCI entry.
        - TrafficGroupId (str(None | /api/v1/sessions/1/ixnetwork/traffic/.../trafficGroup)): The name of the group to which this port is assigned, for the purpose of creating traffic streams among source/destination members of the group.

        Returns
        -------
        - self: This instance with matching fr resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of fr data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the fr resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
