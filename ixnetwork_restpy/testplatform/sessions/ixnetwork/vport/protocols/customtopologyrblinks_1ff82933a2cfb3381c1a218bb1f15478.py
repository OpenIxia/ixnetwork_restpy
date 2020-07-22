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


class CustomTopologyRbLinks(Base):
    """NOT DEFINED
    The CustomTopologyRbLinks class encapsulates a list of customTopologyRbLinks resources that are managed by the user.
    A list of resources can be retrieved from the server using the CustomTopologyRbLinks.find() method.
    The list can be managed by using the CustomTopologyRbLinks.add() and CustomTopologyRbLinks.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'customTopologyRbLinks'
    _SDM_ATT_MAP = {
        'Enabled': 'enabled',
        'LinkMetric': 'linkMetric',
        'LinkNodeSystemId': 'linkNodeSystemId',
    }

    def __init__(self, parent):
        super(CustomTopologyRbLinks, self).__init__(parent)

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
    def LinkMetric(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkMetric'])
    @LinkMetric.setter
    def LinkMetric(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LinkMetric'], value)

    @property
    def LinkNodeSystemId(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['LinkNodeSystemId'])
    @LinkNodeSystemId.setter
    def LinkNodeSystemId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['LinkNodeSystemId'], value)

    def update(self, Enabled=None, LinkMetric=None, LinkNodeSystemId=None):
        """Updates customTopologyRbLinks resource on the server.

        Args
        ----
        - Enabled (bool): NOT DEFINED
        - LinkMetric (number): NOT DEFINED
        - LinkNodeSystemId (str): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Enabled=None, LinkMetric=None, LinkNodeSystemId=None):
        """Adds a new customTopologyRbLinks resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): NOT DEFINED
        - LinkMetric (number): NOT DEFINED
        - LinkNodeSystemId (str): NOT DEFINED

        Returns
        -------
        - self: This instance with all currently retrieved customTopologyRbLinks resources using find and the newly added customTopologyRbLinks resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained customTopologyRbLinks resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, LinkMetric=None, LinkNodeSystemId=None):
        """Finds and retrieves customTopologyRbLinks resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve customTopologyRbLinks resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all customTopologyRbLinks resources from the server.

        Args
        ----
        - Enabled (bool): NOT DEFINED
        - LinkMetric (number): NOT DEFINED
        - LinkNodeSystemId (str): NOT DEFINED

        Returns
        -------
        - self: This instance with matching customTopologyRbLinks resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of customTopologyRbLinks data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the customTopologyRbLinks resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
