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


class DeviceGroup(Base):
    """Describes a set of network devices with similar configuration and the same multiplicity for devices behind.
    The DeviceGroup class encapsulates a list of deviceGroup resources that are managed by the user.
    A list of resources can be retrieved from the server using the DeviceGroup.find() method.
    The list can be managed by using the DeviceGroup.add() and DeviceGroup.remove() methods.
    """

    __slots__ = ()
    _SDM_NAME = 'deviceGroup'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'Enabled': 'enabled',
        'Errors': 'errors',
        'Multiplier': 'multiplier',
        'Name': 'name',
        'Status': 'status',
    }

    def __init__(self, parent):
        super(DeviceGroup, self).__init__(parent)

    @property
    def BfdRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdrouter_deb1cea5df395bf5b6957f7f9cde8ef4.BfdRouter): An instance of the BfdRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bfdrouter_deb1cea5df395bf5b6957f7f9cde8ef4 import BfdRouter
        return BfdRouter(self)

    @property
    def BridgeData(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bridgedata_46f9e50d9befc7b4e2640ba4217a2af2.BridgeData): An instance of the BridgeData class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.bridgedata_46f9e50d9befc7b4e2640ba4217a2af2 import BridgeData
        return BridgeData(self)

    @property
    def DeviceGroup(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.devicegroup_fe4647b311377ec16edf5dcfe93dca09.DeviceGroup): An instance of the DeviceGroup class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.devicegroup_fe4647b311377ec16edf5dcfe93dca09 import DeviceGroup
        return DeviceGroup(self)

    @property
    def Ethernet(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ethernet_18677f1f170027c217563a3250b1f635.Ethernet): An instance of the Ethernet class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ethernet_18677f1f170027c217563a3250b1f635 import Ethernet
        return Ethernet(self)

    @property
    def Ipv4Loopback(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4loopback_f84286c6e2c90f5267670278dde3f258.Ipv4Loopback): An instance of the Ipv4Loopback class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv4loopback_f84286c6e2c90f5267670278dde3f258 import Ipv4Loopback
        return Ipv4Loopback(self)

    @property
    def Ipv6Loopback(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6loopback_c5557054afff2b9cc84b7676de50b805.Ipv6Loopback): An instance of the Ipv6Loopback class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ipv6loopback_c5557054afff2b9cc84b7676de50b805 import Ipv6Loopback
        return Ipv6Loopback(self)

    @property
    def IsisFabricPathRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisfabricpathrouter_3484383ef19d547bbf8b6a3a8701d8ab.IsisFabricPathRouter): An instance of the IsisFabricPathRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisfabricpathrouter_3484383ef19d547bbf8b6a3a8701d8ab import IsisFabricPathRouter
        return IsisFabricPathRouter(self)

    @property
    def IsisL3Router(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3router_502c03d3345feb0ad46b4b9e2d2f2e95.IsisL3Router): An instance of the IsisL3Router class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3router_502c03d3345feb0ad46b4b9e2d2f2e95 import IsisL3Router
        return IsisL3Router(self)

    @property
    def IsisSpbRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbrouter_7f125b55fde121bdcf257dc13c69a82b.IsisSpbRouter): An instance of the IsisSpbRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisspbrouter_7f125b55fde121bdcf257dc13c69a82b import IsisSpbRouter
        return IsisSpbRouter(self)

    @property
    def IsisTrillRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillrouter_a0dffe09cb3b7d2c96fc3b3507112129.IsisTrillRouter): An instance of the IsisTrillRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isistrillrouter_a0dffe09cb3b7d2c96fc3b3507112129 import IsisTrillRouter
        return IsisTrillRouter(self)

    @property
    def LdpBasicRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouter_53e2de40003674322c811a1ba519dbb6.LdpBasicRouter): An instance of the LdpBasicRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouter_53e2de40003674322c811a1ba519dbb6 import LdpBasicRouter
        return LdpBasicRouter(self)

    @property
    def LdpBasicRouterV6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouterv6_b554f464616f39033d7acad4846e556c.LdpBasicRouterV6): An instance of the LdpBasicRouterV6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpbasicrouterv6_b554f464616f39033d7acad4846e556c import LdpBasicRouterV6
        return LdpBasicRouterV6(self)

    @property
    def LdpLpbInterface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldplpbinterface_a8182405aecaf64e394e960bc0e2f18f.LdpLpbInterface): An instance of the LdpLpbInterface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldplpbinterface_a8182405aecaf64e394e960bc0e2f18f import LdpLpbInterface
        return LdpLpbInterface(self)

    @property
    def LdpTargetedRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouter_85c7a9993d80996c22a9dbd739df9692.LdpTargetedRouter): An instance of the LdpTargetedRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouter_85c7a9993d80996c22a9dbd739df9692 import LdpTargetedRouter
        return LdpTargetedRouter(self)

    @property
    def LdpTargetedRouterV6(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouterv6_e86e77f17dfccefac9e15769756089cf.LdpTargetedRouterV6): An instance of the LdpTargetedRouterV6 class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldptargetedrouterv6_e86e77f17dfccefac9e15769756089cf import LdpTargetedRouterV6
        return LdpTargetedRouterV6(self)

    @property
    def Ldpv6LoopbackInterface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpv6loopbackinterface_1c613e9df4bfa76dac19166ff3ca5017.Ldpv6LoopbackInterface): An instance of the Ldpv6LoopbackInterface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ldpv6loopbackinterface_1c613e9df4bfa76dac19166ff3ca5017 import Ldpv6LoopbackInterface
        return Ldpv6LoopbackInterface(self)

    @property
    def MplsoamRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mplsoamrouter_845700fadfdfffc9273541ede90252e5.MplsoamRouter): An instance of the MplsoamRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.mplsoamrouter_845700fadfdfffc9273541ede90252e5 import MplsoamRouter
        return MplsoamRouter(self)

    @property
    def NetworkGroup(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networkgroup_4a63874e791827c3a0361c2d201dbc0c.NetworkGroup): An instance of the NetworkGroup class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networkgroup_4a63874e791827c3a0361c2d201dbc0c import NetworkGroup
        return NetworkGroup(self)

    @property
    def NetworkTopology(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networktopology_657b9792feb17675a34c183046aa9924.NetworkTopology): An instance of the NetworkTopology class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.networktopology_657b9792feb17675a34c183046aa9924 import NetworkTopology
        return NetworkTopology(self)

    @property
    def OfHostData(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ofhostdata_bd823feb7a8ba9bb9ba77fa35a83dce3.OfHostData): An instance of the OfHostData class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ofhostdata_bd823feb7a8ba9bb9ba77fa35a83dce3 import OfHostData
        return OfHostData(self)

    @property
    def Ospfv2Router(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv2router_128102e8c3e6c39adb7b7129aa61b772.Ospfv2Router): An instance of the Ospfv2Router class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv2router_128102e8c3e6c39adb7b7129aa61b772 import Ospfv2Router
        return Ospfv2Router(self)

    @property
    def Ospfv3Router(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3router_b2d6b4f2e4d28091cc2ded1e4203f935.Ospfv3Router): An instance of the Ospfv3Router class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3router_b2d6b4f2e4d28091cc2ded1e4203f935 import Ospfv3Router
        return Ospfv3Router(self)

    @property
    def PimRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimrouter_fdf354c2c4e318a7557c536f097648a7.PimRouter): An instance of the PimRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.pimrouter_fdf354c2c4e318a7557c536f097648a7 import PimRouter
        return PimRouter(self)

    @property
    def RouterData(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.routerdata_48b2bbc3e057b769b893f4a6c10ed927.RouterData): An instance of the RouterData class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.routerdata_48b2bbc3e057b769b893f4a6c10ed927 import RouterData
        return RouterData(self)

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
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def Enabled(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Enables/disables device.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Enabled']))

    @property
    def Errors(self):
        """
        Returns
        -------
        - list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str])): A list of errors that have occurred
        """
        return self._get_attribute(self._SDM_ATT_MAP['Errors'])

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

    @property
    def Status(self):
        """
        Returns
        -------
        - str(configured | error | mixed | notStarted | started | starting | stopping): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Status'])

    def update(self, Multiplier=None, Name=None):
        """Updates deviceGroup resource on the server.

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
        """Adds a new deviceGroup resource on the server and adds it to the container.

        Args
        ----
        - Multiplier (number): Number of device instances per parent device instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with all currently retrieved deviceGroup resources using find and the newly added deviceGroup resources available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._create(self._map_locals(self._SDM_ATT_MAP, locals()))

    def remove(self):
        """Deletes all the contained deviceGroup resources in this instance from the server.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        self._delete()

    def find(self, Count=None, DescriptiveName=None, Errors=None, Multiplier=None, Name=None, Status=None):
        """Finds and retrieves deviceGroup resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve deviceGroup resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all deviceGroup resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        - Errors (list(dict(arg1:str[None | /api/v1/sessions/1/ixnetwork//.../*],arg2:list[str]))): A list of errors that have occurred
        - Multiplier (number): Number of device instances per parent device instance (multiplier)
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - Status (str(configured | error | mixed | notStarted | started | starting | stopping)): Running status of associated network element. Once in Started state, protocol sessions will begin to negotiate.

        Returns
        -------
        - self: This instance with matching deviceGroup resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of deviceGroup data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the deviceGroup resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Enabled=None):
        """Base class infrastructure that gets a list of deviceGroup device ids encapsulated by this object.

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

    def Abort(self, *args, **kwargs):
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        abort(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        abort(SessionIndices=string)
        ----------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('abort', payload=payload, response_object=None)

    def CopyPaste(self, *args, **kwargs):
        """Executes the copyPaste operation on the server.

        Copy this node, paste it behind the destination node and return the newly copied node.

        copyPaste(Arg2=href)list
        ------------------------
        - Arg2 (str(None | /api/v1/sessions/1/ixnetwork//.../*)): The destination node below which the copied node will be pasted
        - Returns list(str[None | /api/v1/sessions/1/ixnetwork//.../*]): The newly copied node.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('copyPaste', payload=payload, response_object=None)

    def FetchAndUpdateConfigFromCloud(self, *args, **kwargs):
        """Executes the fetchAndUpdateConfigFromCloud operation on the server.

        Learn MAC / IP address for a topology running on VM ports, deployed in AWS.

        fetchAndUpdateConfigFromCloud(Mode=string)
        ------------------------------------------
        - Mode (str): Mode. Options are: cmdrefreshall, cmdrefreshmac, cmdrefreshipv4

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self.href }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('fetchAndUpdateConfigFromCloud', payload=payload, response_object=None)

    def RestartDown(self):
        """Executes the restartDown operation on the server.

        Stop and start interfaces and sessions in Device Group that are in 'Down' state.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('restartDown', payload=payload, response_object=None)

    def Start(self, *args, **kwargs):
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        start(SessionIndices=list)
        --------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        start(SessionIndices=string)
        ----------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self, *args, **kwargs):
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stop(SessionIndices=list)
        -------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        stop(SessionIndices=string)
        ---------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)
