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
import sys
from ixnetwork_restpy.base import Base
from ixnetwork_restpy.files import Files

if sys.version_info >= (3, 5):
    from typing import List, Any, Union


class BroadcastDomainV6(Base):
    """BGP V6 Broadcast Domain Configuration
    The BroadcastDomainV6 class encapsulates a required broadcastDomainV6 resource which will be retrieved from the server every time the property is accessed.
    """

    __slots__ = ()
    _SDM_NAME = "broadcastDomainV6"
    _SDM_ATT_MAP = {
        "Active": "active",
        "AdRouteLabel": "adRouteLabel",
        "BVlanId": "bVlanId",
        "BVlanPriority": "bVlanPriority",
        "BVlanTpid": "bVlanTpid",
        "Count": "count",
        "DescriptiveName": "descriptiveName",
        "EnableVlanAwareService": "enableVlanAwareService",
        "EthernetTagId": "ethernetTagId",
        "GroupAddress": "groupAddress",
        "Name": "name",
        "NoOfMacPools": "noOfMacPools",
        "RootAddress": "rootAddress",
        "RsvpP2mpId": "rsvpP2mpId",
        "RsvpP2mpIdAsNumber": "rsvpP2mpIdAsNumber",
        "RsvpTunnelId": "rsvpTunnelId",
        "SenderAddressPRootNodeAddress": "senderAddressPRootNodeAddress",
        "UsebVlan": "usebVlan",
    }
    _SDM_ENUM_MAP = {}

    def __init__(self, parent, list_op=False):
        super(BroadcastDomainV6, self).__init__(parent, list_op)

    @property
    def PnTLVList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pntlvlist_f29efa99695d122f75b5efd68698cd57.PnTLVList): An instance of the PnTLVList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pntlvlist_f29efa99695d122f75b5efd68698cd57 import (
            PnTLVList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PnTLVList", None) is not None:
                return self._properties.get("PnTLVList")
        return PnTLVList(self)

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Active"]))

    @property
    def AdRouteLabel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): AD Route Label
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AdRouteLabel"]))

    @property
    def BVlanId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): B VLAN ID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BVlanId"]))

    @property
    def BVlanPriority(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): B VLAN Priority
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BVlanPriority"]))

    @property
    def BVlanTpid(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): B VLAN TPID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BVlanTpid"]))

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Count"])

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP["DescriptiveName"])

    @property
    def EnableVlanAwareService(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enable VLAN Aware Service
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableVlanAwareService"])
        )

    @property
    def EthernetTagId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Ethernet Tag ID. For VPWS, this acts as VPWS Service ID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["EthernetTagId"]))

    @property
    def GroupAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Group Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["GroupAddress"]))

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP["Name"])

    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["Name"], value)

    @property
    def NoOfMacPools(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Mac Pools
        """
        return self._get_attribute(self._SDM_ATT_MAP["NoOfMacPools"])

    @NoOfMacPools.setter
    def NoOfMacPools(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NoOfMacPools"], value)

    @property
    def RootAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Root Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RootAddress"]))

    @property
    def RsvpP2mpId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RSVP P2MP ID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RsvpP2mpId"]))

    @property
    def RsvpP2mpIdAsNumber(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RSVP P2MP ID as Number
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["RsvpP2mpIdAsNumber"])
        )

    @property
    def RsvpTunnelId(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): RSVP Tunnel ID
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["RsvpTunnelId"]))

    @property
    def SenderAddressPRootNodeAddress(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Sender Address/P-Root Node Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self,
            self._get_attribute(self._SDM_ATT_MAP["SenderAddressPRootNodeAddress"]),
        )

    @property
    def UsebVlan(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Use B-VLAN
        """
        return self._get_attribute(self._SDM_ATT_MAP["UsebVlan"])

    @UsebVlan.setter
    def UsebVlan(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UsebVlan"], value)

    def update(self, Name=None, NoOfMacPools=None, UsebVlan=None):
        # type: (str, int, bool) -> BroadcastDomainV6
        """Updates broadcastDomainV6 resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfMacPools (number): Number of Mac Pools
        - UsebVlan (bool): Use B-VLAN

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(
        self,
        Count=None,
        DescriptiveName=None,
        Name=None,
        NoOfMacPools=None,
        UsebVlan=None,
    ):
        # type: (int, str, str, int, bool) -> BroadcastDomainV6
        """Finds and retrieves broadcastDomainV6 resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve broadcastDomainV6 resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all broadcastDomainV6 resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfMacPools (number): Number of Mac Pools
        - UsebVlan (bool): Use B-VLAN

        Returns
        -------
        - self: This instance with matching broadcastDomainV6 resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of broadcastDomainV6 data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the broadcastDomainV6 resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def AddDeleteTags(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addDeleteTags operation on the server.

        addDeleteTags(Arg2=bool, Arg3=bool, async_operation=bool)
        ---------------------------------------------------------
        - Arg2 (bool):
        - Arg3 (bool):
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("addDeleteTags", payload=payload, response_object=None)

    def AdvertiseAliasing(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the advertiseAliasing operation on the server.

        Advertise Aliasing Per Broadcast Domain.

        advertiseAliasing(Arg2=list, async_operation=bool)list
        ------------------------------------------------------
        - Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("advertiseAliasing", payload=payload, response_object=None)

    def AdvertiseAliasingPerBroadcastDomain(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the advertiseAliasingPerBroadcastDomain operation on the server.

        Advertise Aliasing Per Broadcast Domain

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        advertiseAliasingPerBroadcastDomain(async_operation=bool)
        ---------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        advertiseAliasingPerBroadcastDomain(SessionIndices=list, async_operation=bool)
        ------------------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        advertiseAliasingPerBroadcastDomain(SessionIndices=string, async_operation=bool)
        --------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "advertiseAliasingPerBroadcastDomain", payload=payload, response_object=None
        )

    def PerformActionOnAllObjects(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[str, None]
        """Executes the performActionOnAllObjects operation on the server.

        Action on All Objects

        performActionOnAllObjects(Arg2=string, async_operation=bool)string
        ------------------------------------------------------------------
        - Arg2 (str): Action Name
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns str:

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "performActionOnAllObjects", payload=payload, response_object=None
        )

    def WithdrawAliasing(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the withdrawAliasing operation on the server.

        Withdraw Aliasing Per Broadcast Domain.

        withdrawAliasing(Arg2=list, async_operation=bool)list
        -----------------------------------------------------
        - Arg2 (list(number)): List of indices into the group. An empty list indicates all instances in the group.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("withdrawAliasing", payload=payload, response_object=None)

    def WithdrawAliasingPerBroadcastDomain(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the withdrawAliasingPerBroadcastDomain operation on the server.

        Advertise Aliasing Per Broadcast Domain

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        withdrawAliasingPerBroadcastDomain(async_operation=bool)
        --------------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        withdrawAliasingPerBroadcastDomain(SessionIndices=list, async_operation=bool)
        -----------------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        withdrawAliasingPerBroadcastDomain(SessionIndices=string, async_operation=bool)
        -------------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = {"Arg1": self}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute(
            "withdrawAliasingPerBroadcastDomain", payload=payload, response_object=None
        )

    def get_device_ids(
        self,
        PortNames=None,
        Active=None,
        AdRouteLabel=None,
        BVlanId=None,
        BVlanPriority=None,
        BVlanTpid=None,
        EnableVlanAwareService=None,
        EthernetTagId=None,
        GroupAddress=None,
        RootAddress=None,
        RsvpP2mpId=None,
        RsvpP2mpIdAsNumber=None,
        RsvpTunnelId=None,
        SenderAddressPRootNodeAddress=None,
    ):
        """Base class infrastructure that gets a list of broadcastDomainV6 device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AdRouteLabel (str): optional regex of adRouteLabel
        - BVlanId (str): optional regex of bVlanId
        - BVlanPriority (str): optional regex of bVlanPriority
        - BVlanTpid (str): optional regex of bVlanTpid
        - EnableVlanAwareService (str): optional regex of enableVlanAwareService
        - EthernetTagId (str): optional regex of ethernetTagId
        - GroupAddress (str): optional regex of groupAddress
        - RootAddress (str): optional regex of rootAddress
        - RsvpP2mpId (str): optional regex of rsvpP2mpId
        - RsvpP2mpIdAsNumber (str): optional regex of rsvpP2mpIdAsNumber
        - RsvpTunnelId (str): optional regex of rsvpTunnelId
        - SenderAddressPRootNodeAddress (str): optional regex of senderAddressPRootNodeAddress

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
