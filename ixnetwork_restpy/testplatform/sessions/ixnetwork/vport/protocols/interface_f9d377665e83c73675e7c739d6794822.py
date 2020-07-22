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


class Interface(Base):
    """A set of interfaces to be included in the RIPng router.
    The Interface class encapsulates a list of interface resources that are managed by the user.
    A list of resources can be retrieved from the server using the Interface.find() method.
    The list can be managed by using the Interface.add() and Interface.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'interface'
    _SDM_ATT_MAP = {
        'Enabled': 'enabled',
        'InterfaceId': 'interfaceId',
        'InterfaceMetric': 'interfaceMetric',
        'ResponseMode': 'responseMode',
    }

    def __init__(self, parent):
        super(Interface, self).__init__(parent)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Enables this particular RIPng interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def InterfaceId(self):
        """
        Returns
        -------
        - str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface): The assigned interface ID.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceId'])
    @InterfaceId.setter
    def InterfaceId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceId'], value)

    @property
    def InterfaceMetric(self):
        """
        Returns
        -------
        - number: The value of the metric assigned to this particular interface. This value is added to the RIPng routing metric before transmission on this interface. It allows metrics for routes with the same standard RIPng routing metric to be identified by the particular interface.The default value is'0. Care should be taken so the combined metric value for a route does not exceed 15. A combined metric of 16 or above indicates that the route is unreachable.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterfaceMetric'])
    @InterfaceMetric.setter
    def InterfaceMetric(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterfaceMetric'], value)

    @property
    def ResponseMode(self):
        """
        Returns
        -------
        - str(splitHorizon | noSplitHorizon | poisonReverse): The response mode of the RIPng interface.
        """
        return self._get_attribute(self._SDM_ATT_MAP['ResponseMode'])
    @ResponseMode.setter
    def ResponseMode(self, value):
        self._set_attribute(self._SDM_ATT_MAP['ResponseMode'], value)

    def update(self, Enabled=None, InterfaceId=None, InterfaceMetric=None, ResponseMode=None):
        """Updates interface resource on the server.

        Args
        ----
        - Enabled (bool): Enables this particular RIPng interface.
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): The assigned interface ID.
        - InterfaceMetric (number): The value of the metric assigned to this particular interface. This value is added to the RIPng routing metric before transmission on this interface. It allows metrics for routes with the same standard RIPng routing metric to be identified by the particular interface.The default value is'0. Care should be taken so the combined metric value for a route does not exceed 15. A combined metric of 16 or above indicates that the route is unreachable.
        - ResponseMode (str(splitHorizon | noSplitHorizon | poisonReverse)): The response mode of the RIPng interface.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Enabled=None, InterfaceId=None, InterfaceMetric=None, ResponseMode=None):
        """Adds a new interface resource on the server and adds it to the container.

        Args
        ----
        - Enabled (bool): Enables this particular RIPng interface.
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): The assigned interface ID.
        - InterfaceMetric (number): The value of the metric assigned to this particular interface. This value is added to the RIPng routing metric before transmission on this interface. It allows metrics for routes with the same standard RIPng routing metric to be identified by the particular interface.The default value is'0. Care should be taken so the combined metric value for a route does not exceed 15. A combined metric of 16 or above indicates that the route is unreachable.
        - ResponseMode (str(splitHorizon | noSplitHorizon | poisonReverse)): The response mode of the RIPng interface.

        Returns
        -------
        - self: This instance with all currently retrieved interface resources using find and the newly added interface resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained interface resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Enabled=None, InterfaceId=None, InterfaceMetric=None, ResponseMode=None):
        """Finds and retrieves interface resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve interface resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all interface resources from the server.

        Args
        ----
        - Enabled (bool): Enables this particular RIPng interface.
        - InterfaceId (str(None | /api/v1/sessions/1/ixnetwork/vport/.../interface)): The assigned interface ID.
        - InterfaceMetric (number): The value of the metric assigned to this particular interface. This value is added to the RIPng routing metric before transmission on this interface. It allows metrics for routes with the same standard RIPng routing metric to be identified by the particular interface.The default value is'0. Care should be taken so the combined metric value for a route does not exceed 15. A combined metric of 16 or above indicates that the route is unreachable.
        - ResponseMode (str(splitHorizon | noSplitHorizon | poisonReverse)): The response mode of the RIPng interface.

        Returns
        -------
        - self: This instance with matching interface resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of interface data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the interface resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
