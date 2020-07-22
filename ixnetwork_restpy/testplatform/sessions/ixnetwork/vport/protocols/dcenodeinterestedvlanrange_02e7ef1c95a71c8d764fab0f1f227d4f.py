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


class DceNodeInterestedVlanRange(Base):
    """This object holds a list of DCE Node Interested Vlan Ranges.
    The DceNodeInterestedVlanRange class encapsulates a list of dceNodeInterestedVlanRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the DceNodeInterestedVlanRange.find() method.
    The list can be managed by using the DceNodeInterestedVlanRange.add() and DceNodeInterestedVlanRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dceNodeInterestedVlanRange'
    _SDM_ATT_MAP = {
        'IncludeInLsp': 'includeInLsp',
        'IncludeInMgroupPdu': 'includeInMgroupPdu',
        'IncludeInterestedVlan': 'includeInterestedVlan',
        'InternodeVlanStep': 'internodeVlanStep',
        'M4BitEnabled': 'm4BitEnabled',
        'M6BitEnabled': 'm6BitEnabled',
        'NoOfSpanningTreeRoot': 'noOfSpanningTreeRoot',
        'StartSpanningTreeRootBridgeId': 'startSpanningTreeRootBridgeId',
        'StartVlanId': 'startVlanId',
        'VlanIdCount': 'vlanIdCount',
    }

    def __init__(self, parent):
        super(DceNodeInterestedVlanRange, self).__init__(parent)

    @property
    def IncludeInLsp(self):
        """
        Returns
        -------
        - bool: If true, a custom VLAN is included in the LSP.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeInLsp'])
    @IncludeInLsp.setter
    def IncludeInLsp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeInLsp'], value)

    @property
    def IncludeInMgroupPdu(self):
        """
        Returns
        -------
        - bool: If true, a custom VLAN is included in the MGROUP PDU.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeInMgroupPdu'])
    @IncludeInMgroupPdu.setter
    def IncludeInMgroupPdu(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeInMgroupPdu'], value)

    @property
    def IncludeInterestedVlan(self):
        """
        Returns
        -------
        - bool: If true, the interested VLAN is included.
        """
        return self._get_attribute(self._SDM_ATT_MAP['IncludeInterestedVlan'])
    @IncludeInterestedVlan.setter
    def IncludeInterestedVlan(self, value):
        self._set_attribute(self._SDM_ATT_MAP['IncludeInterestedVlan'], value)

    @property
    def InternodeVlanStep(self):
        """
        Returns
        -------
        - number: It shows the Increment Step of internode Vlan ID. Default is 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['InternodeVlanStep'])
    @InternodeVlanStep.setter
    def InternodeVlanStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['InternodeVlanStep'], value)

    @property
    def M4BitEnabled(self):
        """
        Returns
        -------
        - bool: If true, the M4 bit is enabled.
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
        - bool: If true, the M6 bit is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['M6BitEnabled'])
    @M6BitEnabled.setter
    def M6BitEnabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['M6BitEnabled'], value)

    @property
    def NoOfSpanningTreeRoot(self):
        """
        Returns
        -------
        - number: The number of spanning tree roots for the VLAN.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfSpanningTreeRoot'])
    @NoOfSpanningTreeRoot.setter
    def NoOfSpanningTreeRoot(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfSpanningTreeRoot'], value)

    @property
    def StartSpanningTreeRootBridgeId(self):
        """
        Returns
        -------
        - str: If true, starts the spanning tree root Bridge Id.
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
        - number: The VLAN Id of first VLAN. Default is 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['StartVlanId'])
    @StartVlanId.setter
    def StartVlanId(self, value):
        self._set_attribute(self._SDM_ATT_MAP['StartVlanId'], value)

    @property
    def VlanIdCount(self):
        """
        Returns
        -------
        - number: The count of the VLAN Id.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanIdCount'])
    @VlanIdCount.setter
    def VlanIdCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanIdCount'], value)

    def update(self, IncludeInLsp=None, IncludeInMgroupPdu=None, IncludeInterestedVlan=None, InternodeVlanStep=None, M4BitEnabled=None, M6BitEnabled=None, NoOfSpanningTreeRoot=None, StartSpanningTreeRootBridgeId=None, StartVlanId=None, VlanIdCount=None):
        """Updates dceNodeInterestedVlanRange resource on the server.

        Args
        ----
        - IncludeInLsp (bool): If true, a custom VLAN is included in the LSP.
        - IncludeInMgroupPdu (bool): If true, a custom VLAN is included in the MGROUP PDU.
        - IncludeInterestedVlan (bool): If true, the interested VLAN is included.
        - InternodeVlanStep (number): It shows the Increment Step of internode Vlan ID. Default is 1.
        - M4BitEnabled (bool): If true, the M4 bit is enabled.
        - M6BitEnabled (bool): If true, the M6 bit is enabled.
        - NoOfSpanningTreeRoot (number): The number of spanning tree roots for the VLAN.
        - StartSpanningTreeRootBridgeId (str): If true, starts the spanning tree root Bridge Id.
        - StartVlanId (number): The VLAN Id of first VLAN. Default is 1.
        - VlanIdCount (number): The count of the VLAN Id.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, IncludeInLsp=None, IncludeInMgroupPdu=None, IncludeInterestedVlan=None, InternodeVlanStep=None, M4BitEnabled=None, M6BitEnabled=None, NoOfSpanningTreeRoot=None, StartSpanningTreeRootBridgeId=None, StartVlanId=None, VlanIdCount=None):
        """Adds a new dceNodeInterestedVlanRange resource on the server and adds it to the container.

        Args
        ----
        - IncludeInLsp (bool): If true, a custom VLAN is included in the LSP.
        - IncludeInMgroupPdu (bool): If true, a custom VLAN is included in the MGROUP PDU.
        - IncludeInterestedVlan (bool): If true, the interested VLAN is included.
        - InternodeVlanStep (number): It shows the Increment Step of internode Vlan ID. Default is 1.
        - M4BitEnabled (bool): If true, the M4 bit is enabled.
        - M6BitEnabled (bool): If true, the M6 bit is enabled.
        - NoOfSpanningTreeRoot (number): The number of spanning tree roots for the VLAN.
        - StartSpanningTreeRootBridgeId (str): If true, starts the spanning tree root Bridge Id.
        - StartVlanId (number): The VLAN Id of first VLAN. Default is 1.
        - VlanIdCount (number): The count of the VLAN Id.

        Returns
        -------
        - self: This instance with all currently retrieved dceNodeInterestedVlanRange resources using find and the newly added dceNodeInterestedVlanRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained dceNodeInterestedVlanRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, IncludeInLsp=None, IncludeInMgroupPdu=None, IncludeInterestedVlan=None, InternodeVlanStep=None, M4BitEnabled=None, M6BitEnabled=None, NoOfSpanningTreeRoot=None, StartSpanningTreeRootBridgeId=None, StartVlanId=None, VlanIdCount=None):
        """Finds and retrieves dceNodeInterestedVlanRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dceNodeInterestedVlanRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dceNodeInterestedVlanRange resources from the server.

        Args
        ----
        - IncludeInLsp (bool): If true, a custom VLAN is included in the LSP.
        - IncludeInMgroupPdu (bool): If true, a custom VLAN is included in the MGROUP PDU.
        - IncludeInterestedVlan (bool): If true, the interested VLAN is included.
        - InternodeVlanStep (number): It shows the Increment Step of internode Vlan ID. Default is 1.
        - M4BitEnabled (bool): If true, the M4 bit is enabled.
        - M6BitEnabled (bool): If true, the M6 bit is enabled.
        - NoOfSpanningTreeRoot (number): The number of spanning tree roots for the VLAN.
        - StartSpanningTreeRootBridgeId (str): If true, starts the spanning tree root Bridge Id.
        - StartVlanId (number): The VLAN Id of first VLAN. Default is 1.
        - VlanIdCount (number): The count of the VLAN Id.

        Returns
        -------
        - self: This instance with matching dceNodeInterestedVlanRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dceNodeInterestedVlanRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dceNodeInterestedVlanRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
