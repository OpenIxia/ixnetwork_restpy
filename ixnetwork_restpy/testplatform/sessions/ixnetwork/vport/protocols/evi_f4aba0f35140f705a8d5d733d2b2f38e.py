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


class Evi(Base):
    """Configures EVPN Instances under Ethernet Segment.
    The Evi class encapsulates a list of evi resources that are managed by the user.
    A list of resources can be retrieved from the server using the Evi.find() method.
    The list can be managed by using the Evi.add() and Evi.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = "evi"
    _SDM_ATT_MAP = {
        "AdRouteLabel": "adRouteLabel",
        "AutoConfigureRdEvi": "autoConfigureRdEvi",
        "AutoConfigureRdIpAddress": "autoConfigureRdIpAddress",
        "Enabled": "enabled",
        "ExportTargetList": "exportTargetList",
        "ImportTargetList": "importTargetList",
        "IncludePmsiTunnelAttribute": "includePmsiTunnelAttribute",
        "MplsAssignedUpstreamOrDownStreamLabel": "mplsAssignedUpstreamOrDownStreamLabel",
        "MulticastTunnelType": "multicastTunnelType",
        "RdEvi": "rdEvi",
        "RdIpAddress": "rdIpAddress",
        "RsvpP2mpId": "rsvpP2mpId",
        "RsvpP2mpIdAsNumber": "rsvpP2mpIdAsNumber",
        "RsvpTunnelId": "rsvpTunnelId",
        "UseUpstreamOrDownStreamAssignedLabel": "useUpstreamOrDownStreamAssignedLabel",
        "UseV4MappedV6Address": "useV4MappedV6Address",
    }
    _SDM_ENUM_MAP = {
        "multicastTunnelType": ["rsvpTeP2mp", "mldpP2mp", "ingressReplication"],
    }

    def __init__(self, parent, list_op=False):
        super(Evi, self).__init__(parent, list_op)

    @property
    def AdInclusiveMulticastRouteAttributes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.adinclusivemulticastrouteattributes_cbb2286b138e4134a4fd675abdd1b50f.AdInclusiveMulticastRouteAttributes): An instance of the AdInclusiveMulticastRouteAttributes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.adinclusivemulticastrouteattributes_cbb2286b138e4134a4fd675abdd1b50f import (
            AdInclusiveMulticastRouteAttributes,
        )

        if len(self._object_properties) > 0:
            if (
                self._properties.get("AdInclusiveMulticastRouteAttributes", None)
                is not None
            ):
                return self._properties.get("AdInclusiveMulticastRouteAttributes")
        return AdInclusiveMulticastRouteAttributes(self)._select()

    @property
    def BroadcastDomains(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.broadcastdomains_e0e4233dfafdf70a0eed2ffe3c495b2d.BroadcastDomains): An instance of the BroadcastDomains class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.broadcastdomains_e0e4233dfafdf70a0eed2ffe3c495b2d import (
            BroadcastDomains,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("BroadcastDomains", None) is not None:
                return self._properties.get("BroadcastDomains")
        return BroadcastDomains(self)

    @property
    def EviOpaqueTlv(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.eviopaquetlv_033801b83d5c442510c75fb6d0e848f9.EviOpaqueTlv): An instance of the EviOpaqueTlv class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.vport.protocols.eviopaquetlv_033801b83d5c442510c75fb6d0e848f9 import (
            EviOpaqueTlv,
        )

        if len(self._object_properties) > 0:
            if self._properties.get("EviOpaqueTlv", None) is not None:
                return self._properties.get("EviOpaqueTlv")
        return EviOpaqueTlv(self)

    @property
    def AdRouteLabel(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Label value carried in AD route per EVI. Default value is 16. Minimum value is 16 and maximum value is 0xFFFFF.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AdRouteLabel"])

    @AdRouteLabel.setter
    def AdRouteLabel(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["AdRouteLabel"], value)

    @property
    def AutoConfigureRdEvi(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true then RD EVI part of RD is constructed automatically. If false then RD EVI is taken from user in GUI in RD EVI field. Default value is true.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoConfigureRdEvi"])

    @AutoConfigureRdEvi.setter
    def AutoConfigureRdEvi(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoConfigureRdEvi"], value)

    @property
    def AutoConfigureRdIpAddress(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true then IP address part of RD is constructed automatically and this IP address is taken from loopback address of local BGP peer. If false then IP address is taken from user in GUI in RD IP Address field. Default value is true.
        """
        return self._get_attribute(self._SDM_ATT_MAP["AutoConfigureRdIpAddress"])

    @AutoConfigureRdIpAddress.setter
    def AutoConfigureRdIpAddress(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["AutoConfigureRdIpAddress"], value)

    @property
    def Enabled(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true then this EVI is used in EVPN. Default value is false.
        """
        return self._get_attribute(self._SDM_ATT_MAP["Enabled"])

    @Enabled.setter
    def Enabled(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["Enabled"], value)

    @property
    def ExportTargetList(self):
        """
        Returns
        -------
        - list(dict(arg1:str[as | ip],arg2:number,arg3:str,arg4:number)): NOT DEFINED
        """
        return self._get_attribute(self._SDM_ATT_MAP["ExportTargetList"])

    @ExportTargetList.setter
    def ExportTargetList(self, value):
        self._set_attribute(self._SDM_ATT_MAP["ExportTargetList"], value)

    @property
    def ImportTargetList(self):
        """
        Returns
        -------
        - list(dict(arg1:str[as | ip],arg2:number,arg3:str,arg4:number)): Used to import the routes received from remote peer. Ixia port needs to have at least one export RT of remote peer as import RT.
        """
        return self._get_attribute(self._SDM_ATT_MAP["ImportTargetList"])

    @ImportTargetList.setter
    def ImportTargetList(self, value):
        self._set_attribute(self._SDM_ATT_MAP["ImportTargetList"], value)

    @property
    def IncludePmsiTunnelAttribute(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true then PMSI tunnel attribute is included in Inclusive Multicast Ethernet Tag Route. Default value is false.
        """
        return self._get_attribute(self._SDM_ATT_MAP["IncludePmsiTunnelAttribute"])

    @IncludePmsiTunnelAttribute.setter
    def IncludePmsiTunnelAttribute(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["IncludePmsiTunnelAttribute"], value)

    @property
    def MplsAssignedUpstreamOrDownStreamLabel(self):
        # type: () -> int
        """
        Returns
        -------
        - number: If Use Upstream/Downstream Assigned Label is true then label value mentioned in this field is carried in PMSI tunnel attribute. Default value is 16. Minimum value is 16 and maximum value is 0xFFFFF.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["MplsAssignedUpstreamOrDownStreamLabel"]
        )

    @MplsAssignedUpstreamOrDownStreamLabel.setter
    def MplsAssignedUpstreamOrDownStreamLabel(self, value):
        # type: (int) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["MplsAssignedUpstreamOrDownStreamLabel"], value
        )

    @property
    def MulticastTunnelType(self):
        # type: () -> str
        """
        Returns
        -------
        - str(rsvpTeP2mp | mldpP2mp | ingressReplication): Drop down of {Ingress Replication, RSVP-TE P2MP, mLDP P2MP}. Default value is Ingress Replication.
        """
        return self._get_attribute(self._SDM_ATT_MAP["MulticastTunnelType"])

    @MulticastTunnelType.setter
    def MulticastTunnelType(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["MulticastTunnelType"], value)

    @property
    def RdEvi(self):
        # type: () -> int
        """
        Returns
        -------
        - number: when Auto Configure RD EVI is false then RD EVI part of RD is taken from here. Default value is zero.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RdEvi"])

    @RdEvi.setter
    def RdEvi(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RdEvi"], value)

    @property
    def RdIpAddress(self):
        # type: () -> str
        """
        Returns
        -------
        - str: when Auto Configure RD IP Address is false then IP address part of RD is taken from here. Default value is all zero.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RdIpAddress"])

    @RdIpAddress.setter
    def RdIpAddress(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RdIpAddress"], value)

    @property
    def RsvpP2mpId(self):
        # type: () -> str
        """
        Returns
        -------
        - str: The P2MP Id represented in IP address format. Default value is all zero.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RsvpP2mpId"])

    @RsvpP2mpId.setter
    def RsvpP2mpId(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP["RsvpP2mpId"], value)

    @property
    def RsvpP2mpIdAsNumber(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The P2MP Id represented in integer format. Default value is 0.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RsvpP2mpIdAsNumber"])

    @RsvpP2mpIdAsNumber.setter
    def RsvpP2mpIdAsNumber(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RsvpP2mpIdAsNumber"], value)

    @property
    def RsvpTunnelId(self):
        # type: () -> int
        """
        Returns
        -------
        - number: The Tunnel ID value. Default value is 0. Minimum value is 0 and maximum value is 0xFFFF.
        """
        return self._get_attribute(self._SDM_ATT_MAP["RsvpTunnelId"])

    @RsvpTunnelId.setter
    def RsvpTunnelId(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP["RsvpTunnelId"], value)

    @property
    def UseUpstreamOrDownStreamAssignedLabel(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true then MPLS assigned Upstream/Downstream label is carried in PMSI tunnel attribute else 0 is carried in PMSI tunnel attribute. Default value is true.
        """
        return self._get_attribute(
            self._SDM_ATT_MAP["UseUpstreamOrDownStreamAssignedLabel"]
        )

    @UseUpstreamOrDownStreamAssignedLabel.setter
    def UseUpstreamOrDownStreamAssignedLabel(self, value):
        # type: (bool) -> None
        self._set_attribute(
            self._SDM_ATT_MAP["UseUpstreamOrDownStreamAssignedLabel"], value
        )

    @property
    def UseV4MappedV6Address(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: If true then V4 mapped V6 address is used for tunnel identifier in case of Ingress Replication only.
        """
        return self._get_attribute(self._SDM_ATT_MAP["UseV4MappedV6Address"])

    @UseV4MappedV6Address.setter
    def UseV4MappedV6Address(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP["UseV4MappedV6Address"], value)

    def update(
        self,
        AdRouteLabel=None,
        AutoConfigureRdEvi=None,
        AutoConfigureRdIpAddress=None,
        Enabled=None,
        ExportTargetList=None,
        ImportTargetList=None,
        IncludePmsiTunnelAttribute=None,
        MplsAssignedUpstreamOrDownStreamLabel=None,
        MulticastTunnelType=None,
        RdEvi=None,
        RdIpAddress=None,
        RsvpP2mpId=None,
        RsvpP2mpIdAsNumber=None,
        RsvpTunnelId=None,
        UseUpstreamOrDownStreamAssignedLabel=None,
        UseV4MappedV6Address=None,
    ):
        """Updates evi resource on the server.

        Args
        ----
        - AdRouteLabel (number): Label value carried in AD route per EVI. Default value is 16. Minimum value is 16 and maximum value is 0xFFFFF.
        - AutoConfigureRdEvi (bool): If true then RD EVI part of RD is constructed automatically. If false then RD EVI is taken from user in GUI in RD EVI field. Default value is true.
        - AutoConfigureRdIpAddress (bool): If true then IP address part of RD is constructed automatically and this IP address is taken from loopback address of local BGP peer. If false then IP address is taken from user in GUI in RD IP Address field. Default value is true.
        - Enabled (bool): If true then this EVI is used in EVPN. Default value is false.
        - ExportTargetList (list(dict(arg1:str[as | ip],arg2:number,arg3:str,arg4:number))): NOT DEFINED
        - ImportTargetList (list(dict(arg1:str[as | ip],arg2:number,arg3:str,arg4:number))): Used to import the routes received from remote peer. Ixia port needs to have at least one export RT of remote peer as import RT.
        - IncludePmsiTunnelAttribute (bool): If true then PMSI tunnel attribute is included in Inclusive Multicast Ethernet Tag Route. Default value is false.
        - MplsAssignedUpstreamOrDownStreamLabel (number): If Use Upstream/Downstream Assigned Label is true then label value mentioned in this field is carried in PMSI tunnel attribute. Default value is 16. Minimum value is 16 and maximum value is 0xFFFFF.
        - MulticastTunnelType (str(rsvpTeP2mp | mldpP2mp | ingressReplication)): Drop down of {Ingress Replication, RSVP-TE P2MP, mLDP P2MP}. Default value is Ingress Replication.
        - RdEvi (number): when Auto Configure RD EVI is false then RD EVI part of RD is taken from here. Default value is zero.
        - RdIpAddress (str): when Auto Configure RD IP Address is false then IP address part of RD is taken from here. Default value is all zero.
        - RsvpP2mpId (str): The P2MP Id represented in IP address format. Default value is all zero.
        - RsvpP2mpIdAsNumber (number): The P2MP Id represented in integer format. Default value is 0.
        - RsvpTunnelId (number): The Tunnel ID value. Default value is 0. Minimum value is 0 and maximum value is 0xFFFF.
        - UseUpstreamOrDownStreamAssignedLabel (bool): If true then MPLS assigned Upstream/Downstream label is carried in PMSI tunnel attribute else 0 is carried in PMSI tunnel attribute. Default value is true.
        - UseV4MappedV6Address (bool): If true then V4 mapped V6 address is used for tunnel identifier in case of Ingress Replication only.

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(
        self,
        AdRouteLabel=None,
        AutoConfigureRdEvi=None,
        AutoConfigureRdIpAddress=None,
        Enabled=None,
        ExportTargetList=None,
        ImportTargetList=None,
        IncludePmsiTunnelAttribute=None,
        MplsAssignedUpstreamOrDownStreamLabel=None,
        MulticastTunnelType=None,
        RdEvi=None,
        RdIpAddress=None,
        RsvpP2mpId=None,
        RsvpP2mpIdAsNumber=None,
        RsvpTunnelId=None,
        UseUpstreamOrDownStreamAssignedLabel=None,
        UseV4MappedV6Address=None,
    ):
        """Adds a new evi resource on the server and adds it to the container.

        Args
        ----
        - AdRouteLabel (number): Label value carried in AD route per EVI. Default value is 16. Minimum value is 16 and maximum value is 0xFFFFF.
        - AutoConfigureRdEvi (bool): If true then RD EVI part of RD is constructed automatically. If false then RD EVI is taken from user in GUI in RD EVI field. Default value is true.
        - AutoConfigureRdIpAddress (bool): If true then IP address part of RD is constructed automatically and this IP address is taken from loopback address of local BGP peer. If false then IP address is taken from user in GUI in RD IP Address field. Default value is true.
        - Enabled (bool): If true then this EVI is used in EVPN. Default value is false.
        - ExportTargetList (list(dict(arg1:str[as | ip],arg2:number,arg3:str,arg4:number))): NOT DEFINED
        - ImportTargetList (list(dict(arg1:str[as | ip],arg2:number,arg3:str,arg4:number))): Used to import the routes received from remote peer. Ixia port needs to have at least one export RT of remote peer as import RT.
        - IncludePmsiTunnelAttribute (bool): If true then PMSI tunnel attribute is included in Inclusive Multicast Ethernet Tag Route. Default value is false.
        - MplsAssignedUpstreamOrDownStreamLabel (number): If Use Upstream/Downstream Assigned Label is true then label value mentioned in this field is carried in PMSI tunnel attribute. Default value is 16. Minimum value is 16 and maximum value is 0xFFFFF.
        - MulticastTunnelType (str(rsvpTeP2mp | mldpP2mp | ingressReplication)): Drop down of {Ingress Replication, RSVP-TE P2MP, mLDP P2MP}. Default value is Ingress Replication.
        - RdEvi (number): when Auto Configure RD EVI is false then RD EVI part of RD is taken from here. Default value is zero.
        - RdIpAddress (str): when Auto Configure RD IP Address is false then IP address part of RD is taken from here. Default value is all zero.
        - RsvpP2mpId (str): The P2MP Id represented in IP address format. Default value is all zero.
        - RsvpP2mpIdAsNumber (number): The P2MP Id represented in integer format. Default value is 0.
        - RsvpTunnelId (number): The Tunnel ID value. Default value is 0. Minimum value is 0 and maximum value is 0xFFFF.
        - UseUpstreamOrDownStreamAssignedLabel (bool): If true then MPLS assigned Upstream/Downstream label is carried in PMSI tunnel attribute else 0 is carried in PMSI tunnel attribute. Default value is true.
        - UseV4MappedV6Address (bool): If true then V4 mapped V6 address is used for tunnel identifier in case of Ingress Replication only.

        Returns
        -------
        - self: This instance with all currently retrieved evi resources using find and the newly added evi resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained evi resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(
        self,
        AdRouteLabel=None,
        AutoConfigureRdEvi=None,
        AutoConfigureRdIpAddress=None,
        Enabled=None,
        ExportTargetList=None,
        ImportTargetList=None,
        IncludePmsiTunnelAttribute=None,
        MplsAssignedUpstreamOrDownStreamLabel=None,
        MulticastTunnelType=None,
        RdEvi=None,
        RdIpAddress=None,
        RsvpP2mpId=None,
        RsvpP2mpIdAsNumber=None,
        RsvpTunnelId=None,
        UseUpstreamOrDownStreamAssignedLabel=None,
        UseV4MappedV6Address=None,
    ):
        """Finds and retrieves evi resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve evi resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all evi resources from the server.

        Args
        ----
        - AdRouteLabel (number): Label value carried in AD route per EVI. Default value is 16. Minimum value is 16 and maximum value is 0xFFFFF.
        - AutoConfigureRdEvi (bool): If true then RD EVI part of RD is constructed automatically. If false then RD EVI is taken from user in GUI in RD EVI field. Default value is true.
        - AutoConfigureRdIpAddress (bool): If true then IP address part of RD is constructed automatically and this IP address is taken from loopback address of local BGP peer. If false then IP address is taken from user in GUI in RD IP Address field. Default value is true.
        - Enabled (bool): If true then this EVI is used in EVPN. Default value is false.
        - ExportTargetList (list(dict(arg1:str[as | ip],arg2:number,arg3:str,arg4:number))): NOT DEFINED
        - ImportTargetList (list(dict(arg1:str[as | ip],arg2:number,arg3:str,arg4:number))): Used to import the routes received from remote peer. Ixia port needs to have at least one export RT of remote peer as import RT.
        - IncludePmsiTunnelAttribute (bool): If true then PMSI tunnel attribute is included in Inclusive Multicast Ethernet Tag Route. Default value is false.
        - MplsAssignedUpstreamOrDownStreamLabel (number): If Use Upstream/Downstream Assigned Label is true then label value mentioned in this field is carried in PMSI tunnel attribute. Default value is 16. Minimum value is 16 and maximum value is 0xFFFFF.
        - MulticastTunnelType (str(rsvpTeP2mp | mldpP2mp | ingressReplication)): Drop down of {Ingress Replication, RSVP-TE P2MP, mLDP P2MP}. Default value is Ingress Replication.
        - RdEvi (number): when Auto Configure RD EVI is false then RD EVI part of RD is taken from here. Default value is zero.
        - RdIpAddress (str): when Auto Configure RD IP Address is false then IP address part of RD is taken from here. Default value is all zero.
        - RsvpP2mpId (str): The P2MP Id represented in IP address format. Default value is all zero.
        - RsvpP2mpIdAsNumber (number): The P2MP Id represented in integer format. Default value is 0.
        - RsvpTunnelId (number): The Tunnel ID value. Default value is 0. Minimum value is 0 and maximum value is 0xFFFF.
        - UseUpstreamOrDownStreamAssignedLabel (bool): If true then MPLS assigned Upstream/Downstream label is carried in PMSI tunnel attribute else 0 is carried in PMSI tunnel attribute. Default value is true.
        - UseV4MappedV6Address (bool): If true then V4 mapped V6 address is used for tunnel identifier in case of Ingress Replication only.

        Returns
        -------
        - self: This instance with matching evi resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of evi data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the evi resources from the server available through an iterator or index

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
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("advertiseAliasing", payload=payload, response_object=None)

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
        payload = {"Arg1": self.href}
        for i in range(len(args)):
            payload["Arg%s" % (i + 2)] = args[i]
        for item in kwargs.items():
            payload[item[0]] = item[1]
        return self._execute("withdrawAliasing", payload=payload, response_object=None)
