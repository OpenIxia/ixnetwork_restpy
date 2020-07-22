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


class CeVlanIdRange(Base):
    """It signifies the VLAN ranges configured for a particular EVC.
    The CeVlanIdRange class encapsulates a list of ceVlanIdRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the CeVlanIdRange.find() method.
    The list can be managed by using the CeVlanIdRange.add() and CeVlanIdRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'ceVlanIdRange'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'Enabled': 'enabled',
        'IncrementStep': 'incrementStep',
        'StartVlanId': 'startVlanId',
    }

    def __init__(self, parent):
        super(CeVlanIdRange, self).__init__(parent)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: It signifies the number of Vlan Ids configured for the EVC.
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
        - bool: If enabled, CE VLAN Id range is in effect for the EVC.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def IncrementStep(self):
        """
        Returns
        -------
        - number: It shows the Increment Step of Vlan ID. Default is 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncrementStep'])
    @IncrementStep.setter
    def IncrementStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncrementStep'], value)

    @property
    def StartVlanId(self):
        """
        Returns
        -------
        - number: The VLAN Id of first VLAN. Default is 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartVlanId'])
    @StartVlanId.setter
    def StartVlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartVlanId'], value)

    def update(self, Count=None, Enabled=None, IncrementStep=None, StartVlanId=None):
        """Updates ceVlanIdRange resource on the server.

        Args
        ----
        - Count (number): It signifies the number of Vlan Ids configured for the EVC.
        - Enabled (bool): If enabled, CE VLAN Id range is in effect for the EVC.
        - IncrementStep (number): It shows the Increment Step of Vlan ID. Default is 1.
        - StartVlanId (number): The VLAN Id of first VLAN. Default is 1.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Count=None, Enabled=None, IncrementStep=None, StartVlanId=None):
        """Adds a new ceVlanIdRange resource on the server and adds it to the container.

        Args
        ----
        - Count (number): It signifies the number of Vlan Ids configured for the EVC.
        - Enabled (bool): If enabled, CE VLAN Id range is in effect for the EVC.
        - IncrementStep (number): It shows the Increment Step of Vlan ID. Default is 1.
        - StartVlanId (number): The VLAN Id of first VLAN. Default is 1.

        Returns
        -------
        - self: This instance with all currently retrieved ceVlanIdRange resources using find and the newly added ceVlanIdRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained ceVlanIdRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Count=None, Enabled=None, IncrementStep=None, StartVlanId=None):
        """Finds and retrieves ceVlanIdRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ceVlanIdRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ceVlanIdRange resources from the server.

        Args
        ----
        - Count (number): It signifies the number of Vlan Ids configured for the EVC.
        - Enabled (bool): If enabled, CE VLAN Id range is in effect for the EVC.
        - IncrementStep (number): It shows the Increment Step of Vlan ID. Default is 1.
        - StartVlanId (number): The VLAN Id of first VLAN. Default is 1.

        Returns
        -------
        - self: This instance with matching ceVlanIdRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ceVlanIdRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ceVlanIdRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
