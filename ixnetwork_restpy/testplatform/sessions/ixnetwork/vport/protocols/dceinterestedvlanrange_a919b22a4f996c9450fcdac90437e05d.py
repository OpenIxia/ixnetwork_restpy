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


class DceInterestedVlanRange(Base):
    """This object holds a list of DCE Interested Vlan Ranges.
    The DceInterestedVlanRange class encapsulates a list of dceInterestedVlanRange resources that are managed by the user.
    A list of resources can be retrieved from the server using the DceInterestedVlanRange.find() method.
    The list can be managed by using the DceInterestedVlanRange.add() and DceInterestedVlanRange.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'dceInterestedVlanRange'
    _SDM_ATT_MAP = {
        'EnableIncludeInLsp': 'enableIncludeInLsp',
        'EnableIncludeInMgroupPdu': 'enableIncludeInMgroupPdu',
        'EnableM4Bit': 'enableM4Bit',
        'EnableM6Bit': 'enableM6Bit',
        'Enabled': 'enabled',
        'Nickname': 'nickname',
        'NoOfSpanningTreeRoots': 'noOfSpanningTreeRoots',
        'StartSpanningTreeRootBridgeId': 'startSpanningTreeRootBridgeId',
        'StartVlanId': 'startVlanId',
        'VlanCount': 'vlanCount',
        'VlanIdStep': 'vlanIdStep',
    }

    def __init__(self, parent):
        super(DceInterestedVlanRange, self).__init__(parent)

    @property
    def EnableIncludeInLsp(self):
        """
        Returns
        -------
        - bool: If true, enable a custom VLAN in the LSP.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableIncludeInLsp'])
    @EnableIncludeInLsp.setter
    def EnableIncludeInLsp(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableIncludeInLsp'], value)

    @property
    def EnableIncludeInMgroupPdu(self):
        """
        Returns
        -------
        - bool: If true, enable and include VLAN in Mgroup PDU
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableIncludeInMgroupPdu'])
    @EnableIncludeInMgroupPdu.setter
    def EnableIncludeInMgroupPdu(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableIncludeInMgroupPdu'], value)

    @property
    def EnableM4Bit(self):
        """
        Returns
        -------
        - bool: If true, the M4 bit is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableM4Bit'])
    @EnableM4Bit.setter
    def EnableM4Bit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableM4Bit'], value)

    @property
    def EnableM6Bit(self):
        """
        Returns
        -------
        - bool: If true, the M6 bit is enabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableM6Bit'])
    @EnableM6Bit.setter
    def EnableM6Bit(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableM6Bit'], value)

    @property
    def Enabled(self):
        """
        Returns
        -------
        - bool: Signifies if DCE Interested Vlan range is enabled or disabled.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def Nickname(self):
        """
        Returns
        -------
        - number: The nickname of the VLAN range.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Nickname'])
    @Nickname.setter
    def Nickname(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Nickname'], value)

    @property
    def NoOfSpanningTreeRoots(self):
        """
        Returns
        -------
        - number: The number of spanning tree roots for the VLAN.
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfSpanningTreeRoots'])
    @NoOfSpanningTreeRoots.setter
    def NoOfSpanningTreeRoots(self, value):
        self._set_attribute(self._SDM_ATT_MAP['NoOfSpanningTreeRoots'], value)

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
    def VlanCount(self):
        """
        Returns
        -------
        - number: The count of the VLAN.
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
        - number: It shows the increment step of the VLAN. the default is 1.
        """
        return self._get_attribute(self._SDM_ATT_MAP['VlanIdStep'])
    @VlanIdStep.setter
    def VlanIdStep(self, value):
        self._set_attribute(self._SDM_ATT_MAP['VlanIdStep'], value)

    def update(self, EnableIncludeInLsp=None, EnableIncludeInMgroupPdu=None, EnableM4Bit=None, EnableM6Bit=None, Enabled=None, Nickname=None, NoOfSpanningTreeRoots=None, StartSpanningTreeRootBridgeId=None, StartVlanId=None, VlanCount=None, VlanIdStep=None):
        """Updates dceInterestedVlanRange resource on the server.

        Args
        ----
        - EnableIncludeInLsp (bool): If true, enable a custom VLAN in the LSP.
        - EnableIncludeInMgroupPdu (bool): If true, enable and include VLAN in Mgroup PDU
        - EnableM4Bit (bool): If true, the M4 bit is enabled.
        - EnableM6Bit (bool): If true, the M6 bit is enabled.
        - Enabled (bool): Signifies if DCE Interested Vlan range is enabled or disabled.
        - Nickname (number): The nickname of the VLAN range.
        - NoOfSpanningTreeRoots (number): The number of spanning tree roots for the VLAN.
        - StartSpanningTreeRootBridgeId (str): If true, starts the spanning tree root Bridge Id.
        - StartVlanId (number): The VLAN Id of first VLAN. Default is 1.
        - VlanCount (number): The count of the VLAN.
        - VlanIdStep (number): It shows the increment step of the VLAN. the default is 1.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, EnableIncludeInLsp=None, EnableIncludeInMgroupPdu=None, EnableM4Bit=None, EnableM6Bit=None, Enabled=None, Nickname=None, NoOfSpanningTreeRoots=None, StartSpanningTreeRootBridgeId=None, StartVlanId=None, VlanCount=None, VlanIdStep=None):
        """Adds a new dceInterestedVlanRange resource on the server and adds it to the container.

        Args
        ----
        - EnableIncludeInLsp (bool): If true, enable a custom VLAN in the LSP.
        - EnableIncludeInMgroupPdu (bool): If true, enable and include VLAN in Mgroup PDU
        - EnableM4Bit (bool): If true, the M4 bit is enabled.
        - EnableM6Bit (bool): If true, the M6 bit is enabled.
        - Enabled (bool): Signifies if DCE Interested Vlan range is enabled or disabled.
        - Nickname (number): The nickname of the VLAN range.
        - NoOfSpanningTreeRoots (number): The number of spanning tree roots for the VLAN.
        - StartSpanningTreeRootBridgeId (str): If true, starts the spanning tree root Bridge Id.
        - StartVlanId (number): The VLAN Id of first VLAN. Default is 1.
        - VlanCount (number): The count of the VLAN.
        - VlanIdStep (number): It shows the increment step of the VLAN. the default is 1.

        Returns
        -------
        - self: This instance with all currently retrieved dceInterestedVlanRange resources using find and the newly added dceInterestedVlanRange resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained dceInterestedVlanRange resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, EnableIncludeInLsp=None, EnableIncludeInMgroupPdu=None, EnableM4Bit=None, EnableM6Bit=None, Enabled=None, Nickname=None, NoOfSpanningTreeRoots=None, StartSpanningTreeRootBridgeId=None, StartVlanId=None, VlanCount=None, VlanIdStep=None):
        """Finds and retrieves dceInterestedVlanRange resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve dceInterestedVlanRange resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all dceInterestedVlanRange resources from the server.

        Args
        ----
        - EnableIncludeInLsp (bool): If true, enable a custom VLAN in the LSP.
        - EnableIncludeInMgroupPdu (bool): If true, enable and include VLAN in Mgroup PDU
        - EnableM4Bit (bool): If true, the M4 bit is enabled.
        - EnableM6Bit (bool): If true, the M6 bit is enabled.
        - Enabled (bool): Signifies if DCE Interested Vlan range is enabled or disabled.
        - Nickname (number): The nickname of the VLAN range.
        - NoOfSpanningTreeRoots (number): The number of spanning tree roots for the VLAN.
        - StartSpanningTreeRootBridgeId (str): If true, starts the spanning tree root Bridge Id.
        - StartVlanId (number): The VLAN Id of first VLAN. Default is 1.
        - VlanCount (number): The count of the VLAN.
        - VlanIdStep (number): It shows the increment step of the VLAN. the default is 1.

        Returns
        -------
        - self: This instance with matching dceInterestedVlanRange resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of dceInterestedVlanRange data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the dceInterestedVlanRange resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)
