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


class TrillNodeMacRanges(Base):
    """NOT DEFINED
    The TrillNodeMacRanges class encapsulates a list of trillNodeMacRanges resources that are managed by the user.
    A list of resources can be retrieved from the server using the TrillNodeMacRanges.find() method.
    The list can be managed by using the TrillNodeMacRanges.add() and TrillNodeMacRanges.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'trillNodeMacRanges'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'EnableMacRanges': 'enableMacRanges',
        'InterNodeMacStep': 'interNodeMacStep',
        'StartUnicastMac': 'startUnicastMac',
        'TopologyId': 'topologyId',
        'UnicastMacStep': 'unicastMacStep',
        'VlanId': 'vlanId',
    }

    def __init__(self, parent):
        super(TrillNodeMacRanges, self).__init__(parent)

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
    def EnableMacRanges(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableMacRanges'])
    @EnableMacRanges.setter
    def EnableMacRanges(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableMacRanges'], value)

    @property
    def InterNodeMacStep(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterNodeMacStep'])
    @InterNodeMacStep.setter
    def InterNodeMacStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterNodeMacStep'], value)

    @property
    def StartUnicastMac(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartUnicastMac'])
    @StartUnicastMac.setter
    def StartUnicastMac(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartUnicastMac'], value)

    @property
    def TopologyId(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['TopologyId'])

    @property
    def UnicastMacStep(self):
        """
        Returns
        -------
        - str: NOT DEFINED
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
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanId'])
    @VlanId.setter
    def VlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanId'], value)

    def update(self, Count=None, EnableMacRanges=None, InterNodeMacStep=None, StartUnicastMac=None, UnicastMacStep=None, VlanId=None):
        """Updates trillNodeMacRanges resource on the server.

        Args
        ----
        - Count (number): NOT DEFINED
        - EnableMacRanges (bool): NOT DEFINED
        - InterNodeMacStep (str): NOT DEFINED
        - StartUnicastMac (str): NOT DEFINED
        - UnicastMacStep (str): NOT DEFINED
        - VlanId (number): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Count=None, EnableMacRanges=None, InterNodeMacStep=None, StartUnicastMac=None, UnicastMacStep=None, VlanId=None):
        """Adds a new trillNodeMacRanges resource on the server and adds it to the container.

        Args
        ----
        - Count (number): NOT DEFINED
        - EnableMacRanges (bool): NOT DEFINED
        - InterNodeMacStep (str): NOT DEFINED
        - StartUnicastMac (str): NOT DEFINED
        - UnicastMacStep (str): NOT DEFINED
        - VlanId (number): NOT DEFINED

        Returns
        -------
        - self: This instance with all currently retrieved trillNodeMacRanges resources using find and the newly added trillNodeMacRanges resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained trillNodeMacRanges resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Count=None, EnableMacRanges=None, InterNodeMacStep=None, StartUnicastMac=None, TopologyId=None, UnicastMacStep=None, VlanId=None):
        """Finds and retrieves trillNodeMacRanges resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve trillNodeMacRanges resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all trillNodeMacRanges resources from the server.

        Args
        ----
        - Count (number): NOT DEFINED
        - EnableMacRanges (bool): NOT DEFINED
        - InterNodeMacStep (str): NOT DEFINED
        - StartUnicastMac (str): NOT DEFINED
        - TopologyId (number): NOT DEFINED
        - UnicastMacStep (str): NOT DEFINED
        - VlanId (number): NOT DEFINED

        Returns
        -------
        - self: This instance with matching trillNodeMacRanges resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of trillNodeMacRanges data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the trillNodeMacRanges resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
