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


class SimInterface(Base):
    """Simulated Interface specific configuration inside a Network Topology
    The SimInterface class encapsulates a list of simInterface resources that are managed by the system.
    A list of resources can be retrieved from the server using the SimInterface.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'simInterface'
    _SDM_ATT_MAP = {
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'FromNodeIndex': 'fromNodeIndex',
        'Name': 'name',
        'ToNetworkTopology': 'toNetworkTopology',
        'ToNodeIndex': 'toNodeIndex',
    }

    def __init__(self, parent):
        super(SimInterface, self).__init__(parent)

    @property
    def IsisL3PseudoInterface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3pseudointerface_9126bc028693cbbf9d918cf385cfa24d.IsisL3PseudoInterface): An instance of the IsisL3PseudoInterface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isisl3pseudointerface_9126bc028693cbbf9d918cf385cfa24d import IsisL3PseudoInterface
        return IsisL3PseudoInterface(self)

    @property
    def IsisPseudoInterface(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isispseudointerface_c1f1f37e55c1225f223c72b348d63875.IsisPseudoInterface): An instance of the IsisPseudoInterface class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.isispseudointerface_c1f1f37e55c1225f223c72b348d63875 import IsisPseudoInterface
        return IsisPseudoInterface(self)

    @property
    def SimInterfaceEthernetConfig(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.siminterfaceethernetconfig_1d251364611e333123819f3a7098b591.SimInterfaceEthernetConfig): An instance of the SimInterfaceEthernetConfig class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.siminterfaceethernetconfig_1d251364611e333123819f3a7098b591 import SimInterfaceEthernetConfig
        return SimInterfaceEthernetConfig(self)

    @property
    def SimInterfaceIPv4Config(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.siminterfaceipv4config_e6c1aa40e073d14efc69d40d8efd0f6b.SimInterfaceIPv4Config): An instance of the SimInterfaceIPv4Config class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.siminterfaceipv4config_e6c1aa40e073d14efc69d40d8efd0f6b import SimInterfaceIPv4Config
        return SimInterfaceIPv4Config(self)

    @property
    def SimInterfaceIPv6Config(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.siminterfaceipv6config_189f3bfbc365f2b105e35cd8b9d542d6.SimInterfaceIPv6Config): An instance of the SimInterfaceIPv6Config class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.siminterfaceipv6config_189f3bfbc365f2b105e35cd8b9d542d6 import SimInterfaceIPv6Config
        return SimInterfaceIPv6Config(self)

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
    def FromNodeIndex(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): From Node
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FromNodeIndex']))

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
    def ToNetworkTopology(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Network Topology this link is pointing to
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ToNetworkTopology']))

    @property
    def ToNodeIndex(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): To Node
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ToNodeIndex']))

    def update(self, Name=None):
        """Updates simInterface resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, Name=None):
        """Finds and retrieves simInterface resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve simInterface resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all simInterface resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns
        -------
        - self: This instance with matching simInterface resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of simInterface data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the simInterface resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, FromNodeIndex=None, ToNetworkTopology=None, ToNodeIndex=None):
        """Base class infrastructure that gets a list of simInterface device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - FromNodeIndex (str): optional regex of fromNodeIndex
        - ToNetworkTopology (str): optional regex of toNetworkTopology
        - ToNodeIndex (str): optional regex of toNodeIndex

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
