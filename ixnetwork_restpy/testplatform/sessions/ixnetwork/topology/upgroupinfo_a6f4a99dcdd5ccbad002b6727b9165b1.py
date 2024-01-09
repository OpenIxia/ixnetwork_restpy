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


class UpGroupInfo(Base):
    """UP Group level Configuration
    The UpGroupInfo class encapsulates a list of upGroupInfo resources that are managed by the user.
    A list of resources can be retrieved from the server using the UpGroupInfo.find() method.
    The list can be managed by using the UpGroupInfo.add() and UpGroupInfo.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "upGroupInfo"
    _SDM_ATT_MAP = {
        "Active": "active",
        "AddrAllocAckError": "addrAllocAckError",
        "AddrAllocAckMsg": "addrAllocAckMsg",
        "AddrRelAckError": "addrRelAckError",
        "AddrRelAckMsg": "addrRelAckMsg",
        "AddrRenewAckError": "addrRenewAckError",
        "AddrRenewAckMsg": "addrRenewAckMsg",
        "BurstInterval": "burstInterval",
        "Capabilities": "capabilities",
        "ConfigureCuspChannel": "configureCuspChannel",
        "ConfigureVxlanChannel": "configureVxlanChannel",
        "ConnectedVia": "connectedVia",
        "Count": "count",
        "CpVxlanIPv4Address": "cpVxlanIPv4Address",
        "CpVxlanIPv6Address": "cpVxlanIPv6Address",
        "DeadTimer": "deadTimer",
        "DescriptiveName": "descriptiveName",
        "EnableSyncRequest": "enableSyncRequest",
        "Errors": "errors",
        "EstablishmentTimer": "establishmentTimer",
        "HelloAckError": "helloAckError",
        "HelloAckMsg": "helloAckMsg",
        "HelloVendorID": "helloVendorID",
        "IPv4Address": "iPv4Address",
        "IPv6Address": "iPv6Address",
        "KaTimeoutCount": "kaTimeoutCount",
        "KeepaliveTimer": "keepaliveTimer",
        "Multiplier": "multiplier",
        "Name": "name",
        "NetconfCpIPv4Address": "netconfCpIPv4Address",
        "NumberOfAccessInterfaceConfigs": "numberOfAccessInterfaceConfigs",
        "NumberOfDhcpUsers": "numberOfDhcpUsers",
        "NumberOfIPv4AddressPools": "numberOfIPv4AddressPools",
        "NumberOfL2HqosConfig": "numberOfL2HqosConfig",
        "NumberOfL2tpUsers": "numberOfL2tpUsers",
        "NumberOfL3HqosConfig": "numberOfL3HqosConfig",
        "NumberOfL4HqosConfig": "numberOfL4HqosConfig",
        "NumberOfPppoeUsers": "numberOfPppoeUsers",
        "NumberOfStaticUsers": "numberOfStaticUsers",
        "NumberOfWebPolicyConfig": "numberOfWebPolicyConfig",
        "PacketsPerBurst": "packetsPerBurst",
        "PeVid": "peVid",
        "PeVlanPriority": "peVlanPriority",
        "SessionInfo": "sessionInfo",
        "SessionStatus": "sessionStatus",
        "StackedLayers": "stackedLayers",
        "StateCounts": "stateCounts",
        "Status": "status",
        "SubVersion": "subVersion",
        "SyncReqError": "syncReqError",
        "SyncReqMsg": "syncReqMsg",
        "TxMode": "txMode",
        "Upcapabilities": "upcapabilities",
        "VendorID": "vendorID",
        "Version": "version",
        "Vni": "vni",
        "VxlanIPv4Address": "vxlanIPv4Address",
        "VxlanIPv6Address": "vxlanIPv6Address",
    }
    _SDM_ENUM_MAP = {
        "status": [
            "configured",
            "error",
            "mixed",
            "notStarted",
            "started",
            "starting",
            "stopping",
        ],
    }

    def __init__(self, parent, list_op=False):
        super(UpGroupInfo, self).__init__(parent, list_op)

    @property
    def CuspCPAccessInterfaceConfigList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cuspcpaccessinterfaceconfiglist_f29584fdbf397b7eaaaf4b30da24c4f0.CuspCPAccessInterfaceConfigList): An instance of the CuspCPAccessInterfaceConfigList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cuspcpaccessinterfaceconfiglist_f29584fdbf397b7eaaaf4b30da24c4f0 import (
            CuspCPAccessInterfaceConfigList,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("CuspCPAccessInterfaceConfigList", None)
                is not None
            ):
                return self._properties.get("CuspCPAccessInterfaceConfigList")
        return CuspCPAccessInterfaceConfigList(self)._select()

    @property
    def CuspCPIPv4AddressPoolList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cuspcpipv4addresspoollist_455d9f6528efb822a61db2ff9130065f.CuspCPIPv4AddressPoolList): An instance of the CuspCPIPv4AddressPoolList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cuspcpipv4addresspoollist_455d9f6528efb822a61db2ff9130065f import (
            CuspCPIPv4AddressPoolList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CuspCPIPv4AddressPoolList", None) is not None:
                return self._properties.get("CuspCPIPv4AddressPoolList")
        return CuspCPIPv4AddressPoolList(self)._select()

    @property
    def CuspCPWebPolicyConfigList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cuspcpwebpolicyconfiglist_0f48cf3d55c41393db2f61c60efcf9b8.CuspCPWebPolicyConfigList): An instance of the CuspCPWebPolicyConfigList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.cuspcpwebpolicyconfiglist_0f48cf3d55c41393db2f61c60efcf9b8 import (
            CuspCPWebPolicyConfigList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("CuspCPWebPolicyConfigList", None) is not None:
                return self._properties.get("CuspCPWebPolicyConfigList")
        return CuspCPWebPolicyConfigList(self)._select()

    @property
    def DhcpUsersList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpuserslist_c3a3d3b5bb7a4a92267fb9a903ea682c.DhcpUsersList): An instance of the DhcpUsersList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.dhcpuserslist_c3a3d3b5bb7a4a92267fb9a903ea682c import (
            DhcpUsersList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("DhcpUsersList", None) is not None:
                return self._properties.get("DhcpUsersList")
        return DhcpUsersList(self)._select()

    @property
    def L2HqosConfigList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.l2hqosconfiglist_ad60832e8d7a25f523df493978d207eb.L2HqosConfigList): An instance of the L2HqosConfigList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.l2hqosconfiglist_ad60832e8d7a25f523df493978d207eb import (
            L2HqosConfigList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("L2HqosConfigList", None) is not None:
                return self._properties.get("L2HqosConfigList")
        return L2HqosConfigList(self)._select()

    @property
    def L2tpUsersList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.l2tpuserslist_ce8cd9708539a28d42c5e60e8ee06be6.L2tpUsersList): An instance of the L2tpUsersList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.l2tpuserslist_ce8cd9708539a28d42c5e60e8ee06be6 import (
            L2tpUsersList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("L2tpUsersList", None) is not None:
                return self._properties.get("L2tpUsersList")
        return L2tpUsersList(self)._select()

    @property
    def L3HqosConfigList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.l3hqosconfiglist_e4b7d7588a02ced03144622ed1204c25.L3HqosConfigList): An instance of the L3HqosConfigList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.l3hqosconfiglist_e4b7d7588a02ced03144622ed1204c25 import (
            L3HqosConfigList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("L3HqosConfigList", None) is not None:
                return self._properties.get("L3HqosConfigList")
        return L3HqosConfigList(self)._select()

    @property
    def L4HqosConfigList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.l4hqosconfiglist_2a6816a36136a04d56df7f1df9b0ea06.L4HqosConfigList): An instance of the L4HqosConfigList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.l4hqosconfiglist_2a6816a36136a04d56df7f1df9b0ea06 import (
            L4HqosConfigList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("L4HqosConfigList", None) is not None:
                return self._properties.get("L4HqosConfigList")
        return L4HqosConfigList(self)._select()

    @property
    def LearnedInfo(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo_ff4d5e5643a63bccb40b6cf64fc58100.LearnedInfo): An instance of the LearnedInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.learnedinfo.learnedinfo_ff4d5e5643a63bccb40b6cf64fc58100 import (
            LearnedInfo,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("LearnedInfo", None) is not None:
                return self._properties.get("LearnedInfo")
        return LearnedInfo(self)

    @property
    def PppoEUsersList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pppoeuserslist_403d5b77357bdd46c760bcc6e328f73b.PppoEUsersList): An instance of the PppoEUsersList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pppoeuserslist_403d5b77357bdd46c760bcc6e328f73b import (
            PppoEUsersList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("PppoEUsersList", None) is not None:
                return self._properties.get("PppoEUsersList")
        return PppoEUsersList(self)._select()

    @property
    def StaticUsersList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.staticuserslist_0a954635b5a06973caa3d52037ef1fb4.StaticUsersList): An instance of the StaticUsersList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.staticuserslist_0a954635b5a06973caa3d52037ef1fb4 import (
            StaticUsersList,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("StaticUsersList", None) is not None:
                return self._properties.get("StaticUsersList")
        return StaticUsersList(self)._select()

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Active"]))

    @property
    def AddrAllocAckError(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Error code for Addr Alloc Ack Messge. CODE_SUCCESS - 0 CODE_FAIL - 1 CODE_TLV_UNKNOW - 2 CODE_TLV_LENGTH_ERR - 3 CODE_TLV_ATTR_FAIL - 4 CODE_POOL_MISS - 3001 CODE_POOL_FULL - 3002 Custom value.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AddrAllocAckError"])
        )

    @property
    def AddrAllocAckMsg(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Force error for Addr Alloc Ack Message.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AddrAllocAckMsg"])
        )

    @property
    def AddrRelAckError(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Error code for Addr Rel Ack Messge. CODE_SUCCESS - 0 CODE_FAIL - 1 CODE_TLV_UNKNOW - 2 CODE_TLV_LENGTH_ERR - 3 CODE_TLV_ATTR_FAIL - 4 CODE_POOL_MISS - 3001 CODE_POOL_FULL - 3002 CODE_SUBNET_MISSMATCH - 3003 CODE_SUBNET_CONFLICT - 3004 Custom value.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AddrRelAckError"])
        )

    @property
    def AddrRelAckMsg(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Force error for Addr Rel Ack Message.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["AddrRelAckMsg"]))

    @property
    def AddrRenewAckError(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Error code for Addr Renew Ack Messge. CODE_SUCCESS - 0 CODE_FAIL - 1 CODE_TLV_UNKNOW - 2 CODE_TLV_LENGTH_ERR - 3 CODE_TLV_ATTR_FAIL - 4 CODE_POOL_MISS - 3001 CODE_POOL_FULL - 3002 Custom value.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AddrRenewAckError"])
        )

    @property
    def AddrRenewAckMsg(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Force error for Addr Renew Ack Message.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["AddrRenewAckMsg"])
        )

    @property
    def BurstInterval(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Update Interval.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["BurstInterval"]))

    @property
    def Capabilities(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Negotiate whether the user table sends an ACK or not.0-The CP does not need to wait for a response.1-CP needs to wait for an answer.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Capabilities"]))

    @property
    def ConfigureCuspChannel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure CUSP channel.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ConfigureCuspChannel"])
        )

    @property
    def ConfigureVxlanChannel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure VXLAN channel.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["ConfigureVxlanChannel"])
        )

    @property
    def ConnectedVia(self):
        # type: () -> List[str]
        """DEPRECATED
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology]): List of layers this layer is used to connect with to the wire.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ConnectedVia"])

    @ConnectedVia.setter
    def ConnectedVia(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["ConnectedVia"], value)

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
    def CpVxlanIPv4Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 address of the CP VXLAN.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CpVxlanIPv4Address"])
        )

    @property
    def CpVxlanIPv6Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 address of the CP VXLAN.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["CpVxlanIPv6Address"])
        )

    @property
    def DeadTimer(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Expiry of this timer will close the CUSP session.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["DeadTimer"]))

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
    def EnableSyncRequest(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Send synchronisation request.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EnableSyncRequest"])
        )

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP["Errors"])

    @property
    def EstablishmentTimer(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Time to wait for the session to get established.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["EstablishmentTimer"])
        )

    @property
    def HelloAckError(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Error code for Hello Ack Messge. CODE_SUCCESS - 0 CODE_FAIL - 1 CODE_TLV_UNKNOW - 2 CODE_TLV_LENGTH_ERR - 3 CODE_TLV_ATTR_FAIL - 4 CODE_VERSION_MISSMATCH - 5 Custom value.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HelloAckError"]))

    @property
    def HelloAckMsg(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Force error for Hello Ack Message.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HelloAckMsg"]))

    @property
    def HelloVendorID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Vendor ID to be carried in HELLO message.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["HelloVendorID"]))

    @property
    def IPv4Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 address of the UP.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IPv4Address"]))

    @property
    def IPv6Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): UP IPv6 Address
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["IPv6Address"]))

    @property
    def KaTimeoutCount(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Number of times KA timer would run before being stopped.0 means never timeout.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["KaTimeoutCount"])
        )

    @property
    def KeepaliveTimer(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Interval at which keep alive messages are sent.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["KeepaliveTimer"])
        )

    @property
    def Multiplier(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of layer instances per parent instance (multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP["Multiplier"])

    @Multiplier.setter
    def Multiplier(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Multiplier"], value)

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
    def NetconfCpIPv4Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 address of the CP.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["NetconfCpIPv4Address"])
        )

    @property
    def NumberOfAccessInterfaceConfigs(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of access interfaces to configure.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfAccessInterfaceConfigs"])

    @NumberOfAccessInterfaceConfigs.setter
    def NumberOfAccessInterfaceConfigs(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfAccessInterfaceConfigs"], value)

    @property
    def NumberOfDhcpUsers(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of DHCP Subscriber Groups.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfDhcpUsers"])

    @NumberOfDhcpUsers.setter
    def NumberOfDhcpUsers(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfDhcpUsers"], value)

    @property
    def NumberOfIPv4AddressPools(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of IPv4 Address Pools used for CGN.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfIPv4AddressPools"])

    @NumberOfIPv4AddressPools.setter
    def NumberOfIPv4AddressPools(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfIPv4AddressPools"], value)

    @property
    def NumberOfL2HqosConfig(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of L2 HQoS Config
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfL2HqosConfig"])

    @NumberOfL2HqosConfig.setter
    def NumberOfL2HqosConfig(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfL2HqosConfig"], value)

    @property
    def NumberOfL2tpUsers(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of L2TP Subscriber Groups.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfL2tpUsers"])

    @NumberOfL2tpUsers.setter
    def NumberOfL2tpUsers(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfL2tpUsers"], value)

    @property
    def NumberOfL3HqosConfig(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of L3 HQoS Config
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfL3HqosConfig"])

    @NumberOfL3HqosConfig.setter
    def NumberOfL3HqosConfig(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfL3HqosConfig"], value)

    @property
    def NumberOfL4HqosConfig(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of L4 HQoS Config
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfL4HqosConfig"])

    @property
    def NumberOfPppoeUsers(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of PPPoE Subscriber Groups.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfPppoeUsers"])

    @NumberOfPppoeUsers.setter
    def NumberOfPppoeUsers(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfPppoeUsers"], value)

    @property
    def NumberOfStaticUsers(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Static Subscribers.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfStaticUsers"])

    @NumberOfStaticUsers.setter
    def NumberOfStaticUsers(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfStaticUsers"], value)

    @property
    def NumberOfWebPolicyConfig(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of Web Policies to be configured.
        """
        return self._get_attribute(self._SDM_ATT_MAP["NumberOfWebPolicyConfig"])

    @NumberOfWebPolicyConfig.setter
    def NumberOfWebPolicyConfig(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["NumberOfWebPolicyConfig"], value)

    @property
    def PacketsPerBurst(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Updates per Interval
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PacketsPerBurst"])
        )

    @property
    def PeVid(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PE VLAN ID.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["PeVid"]))

    @property
    def PeVlanPriority(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): PE VLAN Priority.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["PeVlanPriority"])
        )

    @property
    def SessionInfo(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[deadTimerExpiredErr | helloTlvLengthErr | helloVersionMismatchErrTx | kaTlvLengthErr | none]): Logs additional information about the session state.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SessionInfo"])

    @property
    def SessionStatus(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[down | notStarted | up]): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        """
        return self._get_attribute(self._SDM_ATT_MAP["SessionStatus"])

    @property
    def StackedLayers(self):
        # type: () -> List[str]
        """
        Returns
        -------
        - list(str[None | /api/v1/sessions/1/ixnetwork/topology]): List of secondary (many to one) child layer protocols
        """
        return self._get_attribute(self._SDM_ATT_MAP["StackedLayers"])

    @StackedLayers.setter
    def StackedLayers(self, value):
        # type: (List[str]) -> None
        self._set_attribute(self._SDM_ATT_MAP["StackedLayers"], value)

    @property
    def StateCounts(self):
        """
        Returns
        -------
        - dict(total:number,notStarted:number,down:number,up:number): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        """
        return self._get_attribute(self._SDM_ATT_MAP["StateCounts"])

    @property
    def Status(self):
        # type: () -> str
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Status"])

    @property
    def SubVersion(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Sub version number.One version per bit, 0 reserved, starting from 1.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SubVersion"]))

    @property
    def SyncReqError(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Error code for Syn Req Messge. CODE_SUCCESS - 0 CODE_FAIL - 1 CODE_TLV_UNKNOW - 2 CODE_TLV_LENGTH_ERR - 3 CODE_TLV_ATTR_FAIL - 4 CODE_SYNC_NOREADY - 2001 CODE_SYNC_UNSUPPORT - 2002 Custom value.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SyncReqError"]))

    @property
    def SyncReqMsg(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Force error for Sync Req Message.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["SyncReqMsg"]))

    @property
    def TxMode(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Tx Mode of Update Message
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["TxMode"]))

    @property
    def Upcapabilities(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Up Capabilities
        """
        return self._get_attribute(self._SDM_ATT_MAP["Upcapabilities"])

    @Upcapabilities.setter
    def Upcapabilities(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["Upcapabilities"], value)

    @property
    def VendorID(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): FactoryID,reuse the manufacturer definition in Radius.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["VendorID"]))

    @property
    def Version(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): CUSP Protocol Version
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Version"]))

    @property
    def Vni(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): VXLAN ID.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP["Vni"]))

    @property
    def VxlanIPv4Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 address of the UP VXLAN.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VxlanIPv4Address"])
        )

    @property
    def VxlanIPv6Address(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): IPv4 address of the UP VXLAN.
        """
        from ixnetwork_restpy.multivalue import Multivalue

        return Multivalue(
            self, self._get_attribute(self._SDM_ATT_MAP["VxlanIPv6Address"])
        )

    def update(
        self,
        ConnectedVia=None,
        Multiplier=None,
        Name=None,
        NumberOfAccessInterfaceConfigs=None,
        NumberOfDhcpUsers=None,
        NumberOfIPv4AddressPools=None,
        NumberOfL2HqosConfig=None,
        NumberOfL2tpUsers=None,
        NumberOfL3HqosConfig=None,
        NumberOfPppoeUsers=None,
        NumberOfStaticUsers=None,
        NumberOfWebPolicyConfig=None,
        StackedLayers=None,
        Upcapabilities=None,
    ):
        # type: (List[str], int, str, int, int, int, int, int, int, int, int, int, List[str], int) -> UpGroupInfo
        """Updates upGroupInfo resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfAccessInterfaceConfigs (number): Number of access interfaces to configure.
        - NumberOfDhcpUsers (number): Number of DHCP Subscriber Groups.
        - NumberOfIPv4AddressPools (number): Number of IPv4 Address Pools used for CGN.
        - NumberOfL2HqosConfig (number): Number of L2 HQoS Config
        - NumberOfL2tpUsers (number): Number of L2TP Subscriber Groups.
        - NumberOfL3HqosConfig (number): Number of L3 HQoS Config
        - NumberOfPppoeUsers (number): Number of PPPoE Subscriber Groups.
        - NumberOfStaticUsers (number): Number of Static Subscribers.
        - NumberOfWebPolicyConfig (number): Number of Web Policies to be configured.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols
        - Upcapabilities (number): Up Capabilities

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        ConnectedVia=None,
        Multiplier=None,
        Name=None,
        NumberOfAccessInterfaceConfigs=None,
        NumberOfDhcpUsers=None,
        NumberOfIPv4AddressPools=None,
        NumberOfL2HqosConfig=None,
        NumberOfL2tpUsers=None,
        NumberOfL3HqosConfig=None,
        NumberOfPppoeUsers=None,
        NumberOfStaticUsers=None,
        NumberOfWebPolicyConfig=None,
        StackedLayers=None,
        Upcapabilities=None,
    ):
        # type: (List[str], int, str, int, int, int, int, int, int, int, int, int, List[str], int) -> UpGroupInfo
        """Adds a new upGroupInfo resource on the server and adds it to the container.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfAccessInterfaceConfigs (number): Number of access interfaces to configure.
        - NumberOfDhcpUsers (number): Number of DHCP Subscriber Groups.
        - NumberOfIPv4AddressPools (number): Number of IPv4 Address Pools used for CGN.
        - NumberOfL2HqosConfig (number): Number of L2 HQoS Config
        - NumberOfL2tpUsers (number): Number of L2TP Subscriber Groups.
        - NumberOfL3HqosConfig (number): Number of L3 HQoS Config
        - NumberOfPppoeUsers (number): Number of PPPoE Subscriber Groups.
        - NumberOfStaticUsers (number): Number of Static Subscribers.
        - NumberOfWebPolicyConfig (number): Number of Web Policies to be configured.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols
        - Upcapabilities (number): Up Capabilities

        Returns
        -------
        - self: This instance with all currently retrieved upGroupInfo resources using find and the newly added upGroupInfo resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained upGroupInfo resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        ConnectedVia=None,
        Count=None,
        DescriptiveName=None,
        Errors=None,
        Multiplier=None,
        Name=None,
        NumberOfAccessInterfaceConfigs=None,
        NumberOfDhcpUsers=None,
        NumberOfIPv4AddressPools=None,
        NumberOfL2HqosConfig=None,
        NumberOfL2tpUsers=None,
        NumberOfL3HqosConfig=None,
        NumberOfL4HqosConfig=None,
        NumberOfPppoeUsers=None,
        NumberOfStaticUsers=None,
        NumberOfWebPolicyConfig=None,
        SessionInfo=None,
        SessionStatus=None,
        StackedLayers=None,
        StateCounts=None,
        Status=None,
        Upcapabilities=None,
    ):
        """Finds and retrieves upGroupInfo resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve upGroupInfo resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all upGroupInfo resources from the server.

        Args
        ----
        - ConnectedVia (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of layers this layer is used to connect with to the wire.
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork/],arg2:list[str]))): A list of errors that have occurred
        - Multiplier (number): Number of layer instances per parent instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NumberOfAccessInterfaceConfigs (number): Number of access interfaces to configure.
        - NumberOfDhcpUsers (number): Number of DHCP Subscriber Groups.
        - NumberOfIPv4AddressPools (number): Number of IPv4 Address Pools used for CGN.
        - NumberOfL2HqosConfig (number): Number of L2 HQoS Config
        - NumberOfL2tpUsers (number): Number of L2TP Subscriber Groups.
        - NumberOfL3HqosConfig (number): Number of L3 HQoS Config
        - NumberOfL4HqosConfig (number): Number of L4 HQoS Config
        - NumberOfPppoeUsers (number): Number of PPPoE Subscriber Groups.
        - NumberOfStaticUsers (number): Number of Static Subscribers.
        - NumberOfWebPolicyConfig (number): Number of Web Policies to be configured.
        - SessionInfo (list(str[deadTimerExpiredErr | helloTlvLengthErr | helloVersionMismatchErrTx | kaTlvLengthErr | none])): Logs additional information about the session state.
        - SessionStatus (list(str[down | notStarted | up])): Current state of protocol session: Not Started - session negotiation not started, the session is not active yet. Down - actively trying to bring up a protocol session, but negotiation is didn't successfully complete (yet). Up - session came up successfully.
        - StackedLayers (list(str[None | /api/v1/sessions/1/ixnetwork/topology])): List of secondary (many to one) child layer protocols
        - StateCounts (dict(total:number,notStarted:number,down:number,up:number)): A list of values that indicates the total number of sessions, the number of sessions not started, the number of sessions down and the number of sessions that are up
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        - Upcapabilities (number): Up Capabilities

        Returns
        -------
        - self: This instance with matching upGroupInfo resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of upGroupInfo data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the upGroupInfo resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def Abort(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        abort(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        abort(SessionIndices=list, async_operation=bool)
        ------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        abort(SessionIndices=string, async_operation=bool)
        --------------------------------------------------
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
        return self._execute("abort", payload=payload, response_object=None)

    def AddDeleteTags(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the addDeleteTags operation on the server.

        addDeleteTags(Arg2=bool, async_operation=bool)
        ----------------------------------------------
        - Arg2 (bool):
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

    def ClearAllLearnedAssignedInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the clearAllLearnedAssignedInfo operation on the server.

        Clear All Learned Assigned Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        clearAllLearnedAssignedInfo(async_operation=bool)
        -------------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        clearAllLearnedAssignedInfo(SessionIndices=list, async_operation=bool)
        ----------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        clearAllLearnedAssignedInfo(SessionIndices=string, async_operation=bool)
        ------------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        clearAllLearnedAssignedInfo(Arg2=list, async_operation=bool)list
        ----------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
            "clearAllLearnedAssignedInfo", payload=payload, response_object=None
        )

    def GetCGNInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getCGNInfo operation on the server.

        Get CGN Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getCGNInfo(async_operation=bool)
        --------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getCGNInfo(SessionIndices=list, async_operation=bool)
        -----------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getCGNInfo(SessionIndices=string, async_operation=bool)
        -------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getCGNInfo(Arg2=list, async_operation=bool)list
        -----------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute("getCGNInfo", payload=payload, response_object=None)

    def GetDHCPSubscriberInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getDHCPSubscriberInfo operation on the server.

        Get DHCP Subscriber Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getDHCPSubscriberInfo(async_operation=bool)
        -------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getDHCPSubscriberInfo(SessionIndices=list, async_operation=bool)
        ----------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getDHCPSubscriberInfo(SessionIndices=string, async_operation=bool)
        ------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getDHCPSubscriberInfo(Arg2=list, async_operation=bool)list
        ----------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
            "getDHCPSubscriberInfo", payload=payload, response_object=None
        )

    def GetL2TPSubscriberInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getL2TPSubscriberInfo operation on the server.

        Get L2TP Subscriber Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getL2TPSubscriberInfo(async_operation=bool)
        -------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getL2TPSubscriberInfo(SessionIndices=list, async_operation=bool)
        ----------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getL2TPSubscriberInfo(SessionIndices=string, async_operation=bool)
        ------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getL2TPSubscriberInfo(Arg2=list, async_operation=bool)list
        ----------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
            "getL2TPSubscriberInfo", payload=payload, response_object=None
        )

    def GetPPPSubscriberInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the getPPPSubscriberInfo operation on the server.

        Get PPP Subscriber Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getPPPSubscriberInfo(async_operation=bool)
        ------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPPPSubscriberInfo(SessionIndices=list, async_operation=bool)
        ---------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getPPPSubscriberInfo(SessionIndices=string, async_operation=bool)
        -----------------------------------------------------------------
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
            "getPPPSubscriberInfo", payload=payload, response_object=None
        )

    def GetPppSubscriberInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getPppSubscriberInfo operation on the server.

        Fetches Subscriber Learned Info.

        getPppSubscriberInfo(Arg2=list, async_operation=bool)list
        ---------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
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
        return self._execute(
            "getPppSubscriberInfo", payload=payload, response_object=None
        )

    def GetStaticSubscriberInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getStaticSubscriberInfo operation on the server.

        Get Static Subscriber Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getStaticSubscriberInfo(async_operation=bool)
        ---------------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getStaticSubscriberInfo(SessionIndices=list, async_operation=bool)
        ------------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getStaticSubscriberInfo(SessionIndices=string, async_operation=bool)
        --------------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getStaticSubscriberInfo(Arg2=list, async_operation=bool)list
        ------------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
            "getStaticSubscriberInfo", payload=payload, response_object=None
        )

    def GetUPResourceInfo(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the getUPResourceInfo operation on the server.

        Get UP Resource Info

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        getUPResourceInfo(async_operation=bool)
        ---------------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getUPResourceInfo(SessionIndices=list, async_operation=bool)
        ------------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getUPResourceInfo(SessionIndices=string, async_operation=bool)
        --------------------------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        getUPResourceInfo(Arg2=list, async_operation=bool)list
        ------------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.
        - Returns list(str): ID to associate each async action invocation

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
        return self._execute("getUPResourceInfo", payload=payload, response_object=None)

    def RestartDown(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the restartDown operation on the server.

        Stop and start interfaces and sessions that are in Down state.

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        restartDown(async_operation=bool)
        ---------------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        restartDown(SessionIndices=list, async_operation=bool)
        ------------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        restartDown(SessionIndices=string, async_operation=bool)
        --------------------------------------------------------
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
        return self._execute("restartDown", payload=payload, response_object=None)

    def SendKeepAlive(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendKeepAlive operation on the server.

        Send Keep Alive. If user hd stopped, re-start KA else send only once.

        sendKeepAlive(Arg2=list, async_operation=bool)list
        --------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
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
        return self._execute("sendKeepAlive", payload=payload, response_object=None)

    def SendUpdateDeleteBursts(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendUpdateDeleteBursts operation on the server.

        Trigger to send bursts of update delete packets.

        sendUpdateDeleteBursts(Arg2=list, async_operation=bool)list
        -----------------------------------------------------------
        - Arg2 (list(number)): List of indices corresponding to trigger data.
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
        return self._execute(
            "sendUpdateDeleteBursts", payload=payload, response_object=None
        )

    def SendUpdateRequestBursts(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the sendUpdateRequestBursts operation on the server.

        Trigger to send bursts of update request packets.

        sendUpdateRequestBursts(Arg2=list, async_operation=bool)list
        ------------------------------------------------------------
        - Arg2 (list(number)): List of indices corresponding to trigger data.
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
        return self._execute(
            "sendUpdateRequestBursts", payload=payload, response_object=None
        )

    def Start(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(SessionIndices=list, async_operation=bool)
        ------------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        start(SessionIndices=string, async_operation=bool)
        --------------------------------------------------
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
        return self._execute("start", payload=payload, response_object=None)

    def StartKeepAlive(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the startKeepAlive operation on the server.

        Stop sending Keep Alive.

        startKeepAlive(Arg2=list, async_operation=bool)list
        ---------------------------------------------------
        - Arg2 (list(number)): List of indices into the protocol plugin. An empty list indicates all instances in the plugin.
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
        return self._execute("startKeepAlive", payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(async_operation=bool)
        --------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stop(SessionIndices=list, async_operation=bool)
        -----------------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        stop(SessionIndices=string, async_operation=bool)
        -------------------------------------------------
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
        return self._execute("stop", payload=payload, response_object=None)

    def StopUpdateDeleteBursts(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the stopUpdateDeleteBursts operation on the server.

        Trigger to stop bursts of update delete packets.

        stopUpdateDeleteBursts(Arg2=list, async_operation=bool)list
        -----------------------------------------------------------
        - Arg2 (list(number)): List of indices corresponding to trigger data.
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
        return self._execute(
            "stopUpdateDeleteBursts", payload=payload, response_object=None
        )

    def StopUpdateRequestBursts(self, *args, **kwargs):
        # type: (*Any, **Any) -> Union[List[str], None]
        """Executes the stopUpdateRequestBursts operation on the server.

        Trigger to stop bursts of update request packets.

        stopUpdateRequestBursts(Arg2=list, async_operation=bool)list
        ------------------------------------------------------------
        - Arg2 (list(number)): List of indices corresponding to trigger data.
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
        return self._execute(
            "stopUpdateRequestBursts", payload=payload, response_object=None
        )

    def get_device_ids(
        self,
        PortNames=None,
        Active=None,
        AddrAllocAckError=None,
        AddrAllocAckMsg=None,
        AddrRelAckError=None,
        AddrRelAckMsg=None,
        AddrRenewAckError=None,
        AddrRenewAckMsg=None,
        BurstInterval=None,
        Capabilities=None,
        ConfigureCuspChannel=None,
        ConfigureVxlanChannel=None,
        CpVxlanIPv4Address=None,
        CpVxlanIPv6Address=None,
        DeadTimer=None,
        EnableSyncRequest=None,
        EstablishmentTimer=None,
        HelloAckError=None,
        HelloAckMsg=None,
        HelloVendorID=None,
        IPv4Address=None,
        IPv6Address=None,
        KaTimeoutCount=None,
        KeepaliveTimer=None,
        NetconfCpIPv4Address=None,
        PacketsPerBurst=None,
        PeVid=None,
        PeVlanPriority=None,
        SubVersion=None,
        SyncReqError=None,
        SyncReqMsg=None,
        TxMode=None,
        VendorID=None,
        Version=None,
        Vni=None,
        VxlanIPv4Address=None,
        VxlanIPv6Address=None,
    ):
        """Base class infrastructure that gets a list of upGroupInfo device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AddrAllocAckError (str): optional regex of addrAllocAckError
        - AddrAllocAckMsg (str): optional regex of addrAllocAckMsg
        - AddrRelAckError (str): optional regex of addrRelAckError
        - AddrRelAckMsg (str): optional regex of addrRelAckMsg
        - AddrRenewAckError (str): optional regex of addrRenewAckError
        - AddrRenewAckMsg (str): optional regex of addrRenewAckMsg
        - BurstInterval (str): optional regex of burstInterval
        - Capabilities (str): optional regex of capabilities
        - ConfigureCuspChannel (str): optional regex of configureCuspChannel
        - ConfigureVxlanChannel (str): optional regex of configureVxlanChannel
        - CpVxlanIPv4Address (str): optional regex of cpVxlanIPv4Address
        - CpVxlanIPv6Address (str): optional regex of cpVxlanIPv6Address
        - DeadTimer (str): optional regex of deadTimer
        - EnableSyncRequest (str): optional regex of enableSyncRequest
        - EstablishmentTimer (str): optional regex of establishmentTimer
        - HelloAckError (str): optional regex of helloAckError
        - HelloAckMsg (str): optional regex of helloAckMsg
        - HelloVendorID (str): optional regex of helloVendorID
        - IPv4Address (str): optional regex of iPv4Address
        - IPv6Address (str): optional regex of iPv6Address
        - KaTimeoutCount (str): optional regex of kaTimeoutCount
        - KeepaliveTimer (str): optional regex of keepaliveTimer
        - NetconfCpIPv4Address (str): optional regex of netconfCpIPv4Address
        - PacketsPerBurst (str): optional regex of packetsPerBurst
        - PeVid (str): optional regex of peVid
        - PeVlanPriority (str): optional regex of peVlanPriority
        - SubVersion (str): optional regex of subVersion
        - SyncReqError (str): optional regex of syncReqError
        - SyncReqMsg (str): optional regex of syncReqMsg
        - TxMode (str): optional regex of txMode
        - VendorID (str): optional regex of vendorID
        - Version (str): optional regex of version
        - Vni (str): optional regex of vni
        - VxlanIPv4Address (str): optional regex of vxlanIPv4Address
        - VxlanIPv6Address (str): optional regex of vxlanIPv6Address

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
