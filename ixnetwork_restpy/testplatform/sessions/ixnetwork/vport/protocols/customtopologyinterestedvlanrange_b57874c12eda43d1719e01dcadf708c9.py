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


class CustomTopologyInterestedVlanRange(Base):
    """NOT DEFINED
    The CustomTopologyInterestedVlanRange class encapsulates a list of customTopologyInterestedVlanRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the CustomTopologyInterestedVlanRange.find() method.
    The list can be managed by using the CustomTopologyInterestedVlanRange.add() and CustomTopologyInterestedVlanRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'customTopologyInterestedVlanRange'
    _SDM_ATT_MAP = {
        'IncludeInterestedVlan': 'includeInterestedVlan',
        'InterNodeVlanStep': 'interNodeVlanStep',
        'M4BitEnabled': 'm4BitEnabled',
        'M6BitEnabled': 'm6BitEnabled',
        'NumberOfSpanningTreeRoots': 'numberOfSpanningTreeRoots',
        'StartSpanningTreeRootBridgeId': 'startSpanningTreeRootBridgeId',
        'StartVlanId': 'startVlanId',
        'VlanCount': 'vlanCount',
        'VlanIdStep': 'vlanIdStep',
    }

    def __init__(self, parent):
        super(CustomTopologyInterestedVlanRange, self).__init__(parent)

    @property
    def IncludeInterestedVlan(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeInterestedVlan'])
    @IncludeInterestedVlan.setter
    def IncludeInterestedVlan(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeInterestedVlan'], value)

    @property
    def InterNodeVlanStep(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['InterNodeVlanStep'])
    @InterNodeVlanStep.setter
    def InterNodeVlanStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InterNodeVlanStep'], value)

    @property
    def M4BitEnabled(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['M4BitEnabled'])
    @M4BitEnabled.setter
    def M4BitEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['M4BitEnabled'], value)

    @property
    def M6BitEnabled(self):
        """
        Returns
        -------
        - bool: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['M6BitEnabled'])
    @M6BitEnabled.setter
    def M6BitEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['M6BitEnabled'], value)

    @property
    def NumberOfSpanningTreeRoots(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['NumberOfSpanningTreeRoots'])
    @NumberOfSpanningTreeRoots.setter
    def NumberOfSpanningTreeRoots(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NumberOfSpanningTreeRoots'], value)

    @property
    def StartSpanningTreeRootBridgeId(self):
        """
        Returns
        -------
        - str: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartSpanningTreeRootBridgeId'])
    @StartSpanningTreeRootBridgeId.setter
    def StartSpanningTreeRootBridgeId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartSpanningTreeRootBridgeId'], value)

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

    @property
    def VlanCount(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanCount'])
    @VlanCount.setter
    def VlanCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanCount'], value)

    @property
    def VlanIdStep(self):
        """
        Returns
        -------
        - number: NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanIdStep'])
    @VlanIdStep.setter
    def VlanIdStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanIdStep'], value)

    def update(self, IncludeInterestedVlan=None, InterNodeVlanStep=None, M4BitEnabled=None, M6BitEnabled=None, NumberOfSpanningTreeRoots=None, StartSpanningTreeRootBridgeId=None, StartVlanId=None, VlanCount=None, VlanIdStep=None):
        """Updates customTopologyInterestedVlanRange resource on the server.

        Args
        ----
        - IncludeInterestedVlan (bool): NOT DEFINED
        - InterNodeVlanStep (number): NOT DEFINED
        - M4BitEnabled (bool): NOT DEFINED
        - M6BitEnabled (bool): NOT DEFINED
        - NumberOfSpanningTreeRoots (number): NOT DEFINED
        - StartSpanningTreeRootBridgeId (str): NOT DEFINED
        - StartVlanId (number): NOT DEFINED
        - VlanCount (number): NOT DEFINED
        - VlanIdStep (number): NOT DEFINED

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, IncludeInterestedVlan=None, InterNodeVlanStep=None, M4BitEnabled=None, M6BitEnabled=None, NumberOfSpanningTreeRoots=None, StartSpanningTreeRootBridgeId=None, StartVlanId=None, VlanCount=None, VlanIdStep=None):
        """Adds a new customTopologyInterestedVlanRange resource on the server and adds it to the container.

        Args
        ----
        - IncludeInterestedVlan (bool): NOT DEFINED
        - InterNodeVlanStep (number): NOT DEFINED
        - M4BitEnabled (bool): NOT DEFINED
        - M6BitEnabled (bool): NOT DEFINED
        - NumberOfSpanningTreeRoots (number): NOT DEFINED
        - StartSpanningTreeRootBridgeId (str): NOT DEFINED
        - StartVlanId (number): NOT DEFINED
        - VlanCount (number): NOT DEFINED
        - VlanIdStep (number): NOT DEFINED

        Returns
        -------
        - self: This instance with all currently retrieved customTopologyInterestedVlanRange resources using find and the newly added customTopologyInterestedVlanRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained customTopologyInterestedVlanRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, IncludeInterestedVlan=None, InterNodeVlanStep=None, M4BitEnabled=None, M6BitEnabled=None, NumberOfSpanningTreeRoots=None, StartSpanningTreeRootBridgeId=None, StartVlanId=None, VlanCount=None, VlanIdStep=None):
        """Finds and retrieves customTopologyInterestedVlanRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve customTopologyInterestedVlanRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all customTopologyInterestedVlanRange resources from the server.

        Args
        ----
        - IncludeInterestedVlan (bool): NOT DEFINED
        - InterNodeVlanStep (number): NOT DEFINED
        - M4BitEnabled (bool): NOT DEFINED
        - M6BitEnabled (bool): NOT DEFINED
        - NumberOfSpanningTreeRoots (number): NOT DEFINED
        - StartSpanningTreeRootBridgeId (str): NOT DEFINED
        - StartVlanId (number): NOT DEFINED
        - VlanCount (number): NOT DEFINED
        - VlanIdStep (number): NOT DEFINED

        Returns
        -------
        - self: This instance with matching customTopologyInterestedVlanRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of customTopologyInterestedVlanRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the customTopologyInterestedVlanRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
