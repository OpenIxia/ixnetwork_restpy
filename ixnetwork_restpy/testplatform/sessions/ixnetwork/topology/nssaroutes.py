# MIT LICENSE
#
# Copyright 1997 - 2019 by IXIA Keysight
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


class NssaRoutes(Base):
    """OSPFv3 NSSA Routes directly derived from RB class since I could not agree with Options and Link State ID PrefixLen in the OSPFv3 specific base class
    The NssaRoutes class encapsulates a list of nssaRoutes resources that is managed by the system.
    A list of resources can be retrieved from the server using the NssaRoutes.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'nssaRoutes'

    def __init__(self, parent):
        super(NssaRoutes, self).__init__(parent)

    @property
    def Active(self):
        """Whether this is to be advertised or not

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('active')

    @property
    def Algorithm(self):
        """Algorithm

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('algorithm')

    @property
    def ConfigureSIDIndexLabel(self):
        """Lets the corresponding router send Prefix SID. By default, it is selected

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('configureSIDIndexLabel')

    @property
    def Count(self):
        """Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.

        Returns:
            number
        """
        return self._get_attribute('count')

    @property
    def DescriptiveName(self):
        """Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context

        Returns:
            str
        """
        return self._get_attribute('descriptiveName')

    @property
    def EFlag(self):
        """E Flag: Explicit-Null Flag: If set, any upstream neighbor of the Prefix-SID originator MUST replace the Prefix-SID with a Prefix-SID having an Explicit-NULL value (0 for IPv4 and 2 for IPv6) before forwarding the packet

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('eFlag')

    @property
    def ForwardingAddress(self):
        """Forwarding Address of IPv6 NSSA LSAs that will be generated due to this range.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('forwardingAddress')

    @property
    def IncludeForwardingAddress(self):
        """Include Forwarding Address

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('includeForwardingAddress')

    @property
    def LFlag(self):
        """L-Flag: Local Flag. If set, then the value/index carried by the SID has local significance

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('lFlag')

    @property
    def LinkStateId(self):
        """Start Link State Id for the LSAs to be generated for this set of IPv6 NSSA networks.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('linkStateId')

    @property
    def LinkStateIdStep(self):
        """Link State Id Step for the LSAs to be generated for this set of IPv6 NSSA networks.

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('linkStateIdStep')

    @property
    def MFlag(self):
        """M-Flag: Mapping Server Flag: If set, the SID was advertised by a Segment Routing Mapping Server

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('mFlag')

    @property
    def Metric(self):
        """Metric

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('metric')

    @property
    def Name(self):
        """Name of NGPF element, guaranteed to be unique in Scenario

        Returns:
            str
        """
        return self._get_attribute('name')
    @Name.setter
    def Name(self, value):
        self._set_attribute('name', value)

    @property
    def NetworkAddress(self):
        """Prefixes of the simulated IPv6 network

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('networkAddress')

    @property
    def NpFlag(self):
        """NP Flag: No-PHP Flag: If set, then the penultimate hop MUST NOT pop the Prefix-SID before delivering the packet to the node that advertised the Prefix-SID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('npFlag')

    @property
    def Prefix(self):
        """Prefix Length

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('prefix')

    @property
    def Propagate(self):
        """Propagate

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('propagate')

    @property
    def RangeSize(self):
        """Range Size

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('rangeSize')

    @property
    def SidIndexLabel(self):
        """SID/Index/Label value associated with the IGP Prefix segment attached to the specific IPv6 prefix

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sidIndexLabel')

    @property
    def VFlag(self):
        """V-Flag: Value flag. If set, then the SID carries an absolute value label value

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('vFlag')

    def update(self, Name=None):
        """Updates a child instance of nssaRoutes on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args:
            Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def find(self, Count=None, DescriptiveName=None, Name=None):
        """Finds and retrieves nssaRoutes data from the server.

        All named parameters support regex and can be used to selectively retrieve nssaRoutes data from the server.
        By default the find method takes no parameters and will retrieve all nssaRoutes data from the server.

        Args:
            Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
            DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
            Name (str): Name of NGPF element, guaranteed to be unique in Scenario

        Returns:
            self: This instance with matching nssaRoutes data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of nssaRoutes data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the nssaRoutes data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, Algorithm=None, ConfigureSIDIndexLabel=None, EFlag=None, ForwardingAddress=None, IncludeForwardingAddress=None, LFlag=None, LinkStateId=None, LinkStateIdStep=None, MFlag=None, Metric=None, NetworkAddress=None, NpFlag=None, Prefix=None, Propagate=None, RangeSize=None, SidIndexLabel=None, VFlag=None):
        """Base class infrastructure that gets a list of nssaRoutes device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args:
            PortNames (str): optional regex of port names
            Active (str): optional regex of active
            Algorithm (str): optional regex of algorithm
            ConfigureSIDIndexLabel (str): optional regex of configureSIDIndexLabel
            EFlag (str): optional regex of eFlag
            ForwardingAddress (str): optional regex of forwardingAddress
            IncludeForwardingAddress (str): optional regex of includeForwardingAddress
            LFlag (str): optional regex of lFlag
            LinkStateId (str): optional regex of linkStateId
            LinkStateIdStep (str): optional regex of linkStateIdStep
            MFlag (str): optional regex of mFlag
            Metric (str): optional regex of metric
            NetworkAddress (str): optional regex of networkAddress
            NpFlag (str): optional regex of npFlag
            Prefix (str): optional regex of prefix
            Propagate (str): optional regex of propagate
            RangeSize (str): optional regex of rangeSize
            SidIndexLabel (str): optional regex of sidIndexLabel
            VFlag (str): optional regex of vFlag

        Returns:
            list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def Advertise(self, *args, **kwargs):
        """Executes the advertise operation on the server.

        Advertise selected routes

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        advertise()

        advertise(SessionIndices:list)
            Args:
                args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        advertise(SessionIndices:string)
            Args:
                args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('advertise', payload=payload, response_object=None)

    def Start(self):
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('start', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('stop', payload=payload, response_object=None)

    def Withdraw(self, *args, **kwargs):
        """Executes the withdraw operation on the server.

        Withdraw selected routes

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        withdraw()

        withdraw(SessionIndices:list)
            Args:
                args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        withdraw(SessionIndices:string)
            Args:
                args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('withdraw', payload=payload, response_object=None)
