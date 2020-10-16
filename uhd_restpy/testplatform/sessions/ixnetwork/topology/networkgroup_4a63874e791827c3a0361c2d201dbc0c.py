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
from uhd_restpy.base import Base
from uhd_restpy.files import Files


class NetworkGroup(Base):
    """Describes a set of network clouds with similar configuration 

        and the same multiplicity for devices behind.
    The NetworkGroup class encapsulates a list of networkGroup resources that are managed by the user.
    A list of resources can be retrieved from the server using the NetworkGroup.find() method.
    The list can be managed by using the NetworkGroup.add() and NetworkGroup.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'networkGroup'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'Enabled': 'enabled',
        'Multiplier': 'multiplier',
        'Name': 'name',
    }

    def __init__(self, parent):
        super(NetworkGroup, self).__init__(parent)

    @property
    def BgpIPRouteProperty(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpiprouteproperty_ffd9071ae88c6283e9f54ec948882405.BgpIPRouteProperty): An instance of the BgpIPRouteProperty class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpiprouteproperty_ffd9071ae88c6283e9f54ec948882405 import BgpIPRouteProperty
        return BgpIPRouteProperty(self)

    @property
    def BgpL3VpnRouteProperty(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpl3vpnrouteproperty_237e07244aec3d43d528e14380a39eb4.BgpL3VpnRouteProperty): An instance of the BgpL3VpnRouteProperty class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpl3vpnrouteproperty_237e07244aec3d43d528e14380a39eb4 import BgpL3VpnRouteProperty
        return BgpL3VpnRouteProperty(self)

    @property
    def BgpMVpnReceiverSitesIpv4(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnreceiversitesipv4_279b1194a64614140f00d08a876cb61b.BgpMVpnReceiverSitesIpv4): An instance of the BgpMVpnReceiverSitesIpv4 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnreceiversitesipv4_279b1194a64614140f00d08a876cb61b import BgpMVpnReceiverSitesIpv4
        return BgpMVpnReceiverSitesIpv4(self)

    @property
    def BgpMVpnReceiverSitesIpv6(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnreceiversitesipv6_49c886be42acc1f3fc70df1023ccb0bd.BgpMVpnReceiverSitesIpv6): An instance of the BgpMVpnReceiverSitesIpv6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnreceiversitesipv6_49c886be42acc1f3fc70df1023ccb0bd import BgpMVpnReceiverSitesIpv6
        return BgpMVpnReceiverSitesIpv6(self)

    @property
    def BgpMVpnSenderSitesIpv4(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnsendersitesipv4_4fb28863ad3595e11a7fecc4fbb6ec9d.BgpMVpnSenderSitesIpv4): An instance of the BgpMVpnSenderSitesIpv4 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnsendersitesipv4_4fb28863ad3595e11a7fecc4fbb6ec9d import BgpMVpnSenderSitesIpv4
        return BgpMVpnSenderSitesIpv4(self)

    @property
    def BgpMVpnSenderSitesIpv6(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnsendersitesipv6_3217a8473cfbb135fc2545010c09ffb6.BgpMVpnSenderSitesIpv6): An instance of the BgpMVpnSenderSitesIpv6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpmvpnsendersitesipv6_3217a8473cfbb135fc2545010c09ffb6 import BgpMVpnSenderSitesIpv6
        return BgpMVpnSenderSitesIpv6(self)

    @property
    def BgpV6IPRouteProperty(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpv6iprouteproperty_3bc5aff598784532c6b5ff0b601d2985.BgpV6IPRouteProperty): An instance of the BgpV6IPRouteProperty class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpv6iprouteproperty_3bc5aff598784532c6b5ff0b601d2985 import BgpV6IPRouteProperty
        return BgpV6IPRouteProperty(self)

    @property
    def BgpV6L3VpnRouteProperty(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpv6l3vpnrouteproperty_f7d29da5d82b8aa29c3f1f6dd1e5780f.BgpV6L3VpnRouteProperty): An instance of the BgpV6L3VpnRouteProperty class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.bgpv6l3vpnrouteproperty_f7d29da5d82b8aa29c3f1f6dd1e5780f import BgpV6L3VpnRouteProperty
        return BgpV6L3VpnRouteProperty(self)

    @property
    def CMacProperties(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties_4ac468c2f246fc5ef1a77fc3e4ebe180.CMacProperties): An instance of the CMacProperties class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.cmacproperties_4ac468c2f246fc5ef1a77fc3e4ebe180 import CMacProperties
        return CMacProperties(self)

    @property
    def DeviceGroup(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.devicegroup_fe4647b311377ec16edf5dcfe93dca09.DeviceGroup): An instance of the DeviceGroup class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.devicegroup_fe4647b311377ec16edf5dcfe93dca09 import DeviceGroup
        return DeviceGroup(self)

    @property
    def DslPools(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.dslpools_d9b929e10c822a015fb7026b5bad393a.DslPools): An instance of the DslPools class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.dslpools_d9b929e10c822a015fb7026b5bad393a import DslPools
        return DslPools(self)

    @property
    def ECpriReRadioChannelsOrUsers(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.ecprireradiochannelsorusers_d1f6861b47ba784e3298939a333f12b9.ECpriReRadioChannelsOrUsers): An instance of the ECpriReRadioChannelsOrUsers class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.ecprireradiochannelsorusers_d1f6861b47ba784e3298939a333f12b9 import ECpriReRadioChannelsOrUsers
        return ECpriReRadioChannelsOrUsers(self)

    @property
    def ECpriRecRadioChannelsOrUsers(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.ecprirecradiochannelsorusers_5814e34000b9bdc960142e49f7af3c67.ECpriRecRadioChannelsOrUsers): An instance of the ECpriRecRadioChannelsOrUsers class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.ecprirecradiochannelsorusers_5814e34000b9bdc960142e49f7af3c67 import ECpriRecRadioChannelsOrUsers
        return ECpriRecRadioChannelsOrUsers(self)

    @property
    def EvpnIPv4PrefixRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange_79e14e1ab070701ebf4eb586cecc565f.EvpnIPv4PrefixRange): An instance of the EvpnIPv4PrefixRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.evpnipv4prefixrange_79e14e1ab070701ebf4eb586cecc565f import EvpnIPv4PrefixRange
        return EvpnIPv4PrefixRange(self)

    @property
    def EvpnIPv6PrefixRange(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange_f8dd80c93700c982de65324fe6552b86.EvpnIPv6PrefixRange): An instance of the EvpnIPv6PrefixRange class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.evpnipv6prefixrange_f8dd80c93700c982de65324fe6552b86 import EvpnIPv6PrefixRange
        return EvpnIPv6PrefixRange(self)

    @property
    def Ipv4PrefixPools(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.ipv4prefixpools_2d6f2aedde61c058965d4e1b21741352.Ipv4PrefixPools): An instance of the Ipv4PrefixPools class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.ipv4prefixpools_2d6f2aedde61c058965d4e1b21741352 import Ipv4PrefixPools
        return Ipv4PrefixPools(self)

    @property
    def Ipv6PrefixPools(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.ipv6prefixpools_f83aba85ff769655b348dc60ddcb30f2.Ipv6PrefixPools): An instance of the Ipv6PrefixPools class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.ipv6prefixpools_f83aba85ff769655b348dc60ddcb30f2 import Ipv6PrefixPools
        return Ipv6PrefixPools(self)

    @property
    def IsisL3RouteProperty(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.isisl3routeproperty_a6c8c14dbcd51f5aa443f5e32d58e8f0.IsisL3RouteProperty): An instance of the IsisL3RouteProperty class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.isisl3routeproperty_a6c8c14dbcd51f5aa443f5e32d58e8f0 import IsisL3RouteProperty
        return IsisL3RouteProperty(self)

    @property
    def IsisSpbMacCloudConfig(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.isisspbmaccloudconfig_791b0bf61c8f6877cabfa2621478ab8a.IsisSpbMacCloudConfig): An instance of the IsisSpbMacCloudConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.isisspbmaccloudconfig_791b0bf61c8f6877cabfa2621478ab8a import IsisSpbMacCloudConfig
        return IsisSpbMacCloudConfig(self)

    @property
    def IsisTrillUCastMacConfig(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.isistrillucastmacconfig_a91c5b3e28b2bee04ff08d2e22fad1e2.IsisTrillUCastMacConfig): An instance of the IsisTrillUCastMacConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.isistrillucastmacconfig_a91c5b3e28b2bee04ff08d2e22fad1e2 import IsisTrillUCastMacConfig
        return IsisTrillUCastMacConfig(self)

    @property
    def LdpFECProperty(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.ldpfecproperty_9d07999903dc2acadf9a2f44f8a94399.LdpFECProperty): An instance of the LdpFECProperty class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.ldpfecproperty_9d07999903dc2acadf9a2f44f8a94399 import LdpFECProperty
        return LdpFECProperty(self)

    @property
    def LdpIpv6FECProperty(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.ldpipv6fecproperty_408cfe80a37623da202d7739fba9b830.LdpIpv6FECProperty): An instance of the LdpIpv6FECProperty class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.ldpipv6fecproperty_408cfe80a37623da202d7739fba9b830 import LdpIpv6FECProperty
        return LdpIpv6FECProperty(self)

    @property
    def MacPools(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.macpools_414597218f17eaa9c882bf703e2d0bdd.MacPools): An instance of the MacPools class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.macpools_414597218f17eaa9c882bf703e2d0bdd import MacPools
        return MacPools(self)

    @property
    def NetworkGroup(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.networkgroup_4a63874e791827c3a0361c2d201dbc0c.NetworkGroup): An instance of the NetworkGroup class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.networkgroup_4a63874e791827c3a0361c2d201dbc0c import NetworkGroup
        return NetworkGroup(self)

    @property
    def NetworkRangeInfo(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.networkrangeinfo_cbb1e7fa358c353ee8fd62246a36a824.NetworkRangeInfo): An instance of the NetworkRangeInfo class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.networkrangeinfo_cbb1e7fa358c353ee8fd62246a36a824 import NetworkRangeInfo
        return NetworkRangeInfo(self)

    @property
    def NetworkTopology(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.networktopology_657b9792feb17675a34c183046aa9924.NetworkTopology): An instance of the NetworkTopology class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.networktopology_657b9792feb17675a34c183046aa9924 import NetworkTopology
        return NetworkTopology(self)

    @property
    def OspfRouteProperty(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.ospfrouteproperty_0f1d984feaec22ff3b59493bc50ee303.OspfRouteProperty): An instance of the OspfRouteProperty class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.ospfrouteproperty_0f1d984feaec22ff3b59493bc50ee303 import OspfRouteProperty
        return OspfRouteProperty(self)

    @property
    def Ospfv3RouteProperty(self):
        """
        Returns
        -------
        - obj(uhd_restpy.testplatform.sessions.ixnetwork.topology.ospfv3routeproperty_daf6d024b6ece255d2d043618b13bae5.Ospfv3RouteProperty): An instance of the Ospfv3RouteProperty class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from uhd_restpy.testplatform.sessions.ixnetwork.topology.ospfv3routeproperty_daf6d024b6ece255d2d043618b13bae5 import Ospfv3RouteProperty
        return Ospfv3RouteProperty(self)

    @property
    def Count(self):
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DescriptiveName(self):
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def Enabled(self):
        """
        Returns
        -------
        - obj(uhd_restpy.multivalue.Multivalue): Enables/disables device.
        """
        from uhd_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Enabled']))

    @property
    def Multiplier(self):
        """
        Returns
        -------
        - number: Number of device instances per parent device instance (multiplier)
        """
        return self._get_attribute(self._SDM_ATT_MAP['Multiplier'])
    @Multiplier.setter
    def Multiplier(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Multiplier'], value)

    @property
    def Name(self):
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    def update(self, Multiplier=None, Name=None):
        """Updates networkGroup resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Multiplier (number): Number of device instances per parent device instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, Multiplier=None, Name=None):
        """Adds a new networkGroup resource on the server and adds it to the container.

        Args
        ----
        - Multiplier (number): Number of device instances per parent device instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with all currently retrieved networkGroup resources using find and the newly added networkGroup resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained networkGroup resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Count=None, DescriptiveName=None, Multiplier=None, Name=None):
        """Finds and retrieves networkGroup resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve networkGroup resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all networkGroup resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Multiplier (number): Number of device instances per parent device instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with matching networkGroup resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of networkGroup data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the networkGroup resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Enabled=None):
        """Base class infrastructure that gets a list of networkGroup device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Enabled (str): optional regex of enabled

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def Abort(self):
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('abort', payload=payload, response_object=None)

    def Start(self):
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('stop', payload=payload, response_object=None)
