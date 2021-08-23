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
from typing import List, Any, Union


class BroadcastDomains(Base):
    """Configures Broadcast Domains under EVI.
    The BroadcastDomains class encapsulates a list of broadcastDomains resources that are managed by the user.
    A list of resources can be retrieved from the server using the BroadcastDomains.find() method.
    The list can be managed by using the BroadcastDomains.add() and BroadcastDomains.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'broadcastDomains'
    _SDM_ATT_MAP = {
        'AdRouteLabel': 'adRouteLabel',
        'BVlanId': 'bVlanId',
        'BVlanPriority': 'bVlanPriority',
        'BVlanTpId': 'bVlanTpId',
        'Enabled': 'enabled',
        'EthernetTagId': 'ethernetTagId',
    }
    _SDM_ENUM_MAP = {
        'bVlanTpId': ['0x8100', '0x9100', '0x9200', '0x88A8'],
    }

    def __init__(self, parent, list_op=False):
        super(BroadcastDomains, self).__init__(parent, list_op)

    @property
    def CMacRange(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.cmacrange_8ee0ca3976d10bdf7e1defed5469922a.CMacRange): An instance of the CMacRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.cmacrange_8ee0ca3976d10bdf7e1defed5469922a import CMacRange
        if self._properties.get('CMacRange', None) is not None:
            return self._properties.get('CMacRange')
        else:
            return CMacRange(self)

    @property
    def AdRouteLabel(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Label value carried in AD route per Broadcast Domain. Default value is 16. Minimum value is 16 and maximum value is 0xFFFFF.
        """
        return self._get_attribute(self._SDM_ATT_MAP['AdRouteLabel'])
    @AdRouteLabel.setter
    def AdRouteLabel(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['AdRouteLabel'], value)

    @property
    def BVlanId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: B-VLAN Identifier used for PBB-EVPN traffic. Default value is 1. Minimum value is 0 and maximum value is 4095.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BVlanId'])
    @BVlanId.setter
    def BVlanId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['BVlanId'], value)

    @property
    def BVlanPriority(self):
        # type: () -> int
        """
        Returns
        -------
        - number: B-VLAN Priority used for PBB-EVPN traffic. Default value is 0. Minimum value is 0 and maximum value is 7.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BVlanPriority'])
    @BVlanPriority.setter
    def BVlanPriority(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['BVlanPriority'], value)

    @property
    def BVlanTpId(self):
        # type: () -> str
        """
        Returns
        -------
        - str(0x8100 | 0x9100 | 0x9200 | 0x88A8): B-VLAN TPID used for PBB-EVPN traffic. Default value is 0x8100. User can select any one of {0x8100, 0x9100, 0x9200, 0x88A8}.
        """
        return self._get_attribute(self._SDM_ATT_MAP['BVlanTpId'])
    @BVlanTpId.setter
    def BVlanTpId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['BVlanTpId'], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true then Broadcast Domain is used in EVPN.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Enabled'])
    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['Enabled'], value)

    @property
    def EthernetTagId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Ethernet Tag Id of an EVI. This can be I-SID, VLAN. Default value is 1. Minimum value is 0 and maximum value is 0xFFFFFFFF.
        """
        return self._get_attribute(self._SDM_ATT_MAP['EthernetTagId'])
    @EthernetTagId.setter
    def EthernetTagId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['EthernetTagId'], value)

    def update(self, AdRouteLabel=None, BVlanId=None, BVlanPriority=None, BVlanTpId=None, Enabled=None, EthernetTagId=None):
        # type: (int, int, int, str, bool, int) -> BroadcastDomains
        """Updates broadcastDomains resource on the server.

        Args
        ----
        - AdRouteLabel (number): Label value carried in AD route per Broadcast Domain. Default value is 16. Minimum value is 16 and maximum value is 0xFFFFF.
        - BVlanId (number): B-VLAN Identifier used for PBB-EVPN traffic. Default value is 1. Minimum value is 0 and maximum value is 4095.
        - BVlanPriority (number): B-VLAN Priority used for PBB-EVPN traffic. Default value is 0. Minimum value is 0 and maximum value is 7.
        - BVlanTpId (str(0x8100 | 0x9100 | 0x9200 | 0x88A8)): B-VLAN TPID used for PBB-EVPN traffic. Default value is 0x8100. User can select any one of {0x8100, 0x9100, 0x9200, 0x88A8}.
        - Enabled (bool): If true then Broadcast Domain is used in EVPN.
        - EthernetTagId (number): Ethernet Tag Id of an EVI. This can be I-SID, VLAN. Default value is 1. Minimum value is 0 and maximum value is 0xFFFFFFFF.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, AdRouteLabel=None, BVlanId=None, BVlanPriority=None, BVlanTpId=None, Enabled=None, EthernetTagId=None):
        # type: (int, int, int, str, bool, int) -> BroadcastDomains
        """Adds a new broadcastDomains resource on the server and adds it to the container.

        Args
        ----
        - AdRouteLabel (number): Label value carried in AD route per Broadcast Domain. Default value is 16. Minimum value is 16 and maximum value is 0xFFFFF.
        - BVlanId (number): B-VLAN Identifier used for PBB-EVPN traffic. Default value is 1. Minimum value is 0 and maximum value is 4095.
        - BVlanPriority (number): B-VLAN Priority used for PBB-EVPN traffic. Default value is 0. Minimum value is 0 and maximum value is 7.
        - BVlanTpId (str(0x8100 | 0x9100 | 0x9200 | 0x88A8)): B-VLAN TPID used for PBB-EVPN traffic. Default value is 0x8100. User can select any one of {0x8100, 0x9100, 0x9200, 0x88A8}.
        - Enabled (bool): If true then Broadcast Domain is used in EVPN.
        - EthernetTagId (number): Ethernet Tag Id of an EVI. This can be I-SID, VLAN. Default value is 1. Minimum value is 0 and maximum value is 0xFFFFFFFF.

        Returns
        -------
        - self: This instance with all currently retrieved broadcastDomains resources using find and the newly added broadcastDomains resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained broadcastDomains resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, AdRouteLabel=None, BVlanId=None, BVlanPriority=None, BVlanTpId=None, Enabled=None, EthernetTagId=None):
        # type: (int, int, int, str, bool, int) -> BroadcastDomains
        """Finds and retrieves broadcastDomains resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve broadcastDomains resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all broadcastDomains resources from the server.

        Args
        ----
        - AdRouteLabel (number): Label value carried in AD route per Broadcast Domain. Default value is 16. Minimum value is 16 and maximum value is 0xFFFFF.
        - BVlanId (number): B-VLAN Identifier used for PBB-EVPN traffic. Default value is 1. Minimum value is 0 and maximum value is 4095.
        - BVlanPriority (number): B-VLAN Priority used for PBB-EVPN traffic. Default value is 0. Minimum value is 0 and maximum value is 7.
        - BVlanTpId (str(0x8100 | 0x9100 | 0x9200 | 0x88A8)): B-VLAN TPID used for PBB-EVPN traffic. Default value is 0x8100. User can select any one of {0x8100, 0x9100, 0x9200, 0x88A8}.
        - Enabled (bool): If true then Broadcast Domain is used in EVPN.
        - EthernetTagId (number): Ethernet Tag Id of an EVI. This can be I-SID, VLAN. Default value is 1. Minimum value is 0 and maximum value is 0xFFFFFFFF.

        Returns
        -------
        - self: This instance with matching broadcastDomains resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of broadcastDomains data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the broadcastDomains resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AdvertiseAliasing(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the advertiseAliasing operation on the server.

        NOT DEFINED

        advertiseAliasing(async_operation=bool)string
        ---------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('advertiseAliasing', payload=payload, response_object=None)

    def WithdrawAliasing(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the withdrawAliasing operation on the server.

        NOT DEFINED

        withdrawAliasing(async_operation=bool)string
        --------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str: NOT DEFINED

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('withdrawAliasing', payload=payload, response_object=None)
