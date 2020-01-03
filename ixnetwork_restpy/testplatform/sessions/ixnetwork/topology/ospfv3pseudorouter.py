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


class Ospfv3PseudoRouter(Base):
    """Simulated Router Information
    The Ospfv3PseudoRouter class encapsulates a list of ospfv3PseudoRouter resources that is managed by the system.
    A list of resources can be retrieved from the server using the Ospfv3PseudoRouter.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'ospfv3PseudoRouter'

    def __init__(self, parent):
        super(Ospfv3PseudoRouter, self).__init__(parent)

    @property
    def ExternalRoutes(self):
        """An instance of the ExternalRoutes class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.externalroutes.ExternalRoutes)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.externalroutes import ExternalRoutes
        return ExternalRoutes(self)

    @property
    def InterAreaPrefix(self):
        """An instance of the InterAreaPrefix class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.interareaprefix.InterAreaPrefix)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.interareaprefix import InterAreaPrefix
        return InterAreaPrefix(self)

    @property
    def InterAreaRouter(self):
        """An instance of the InterAreaRouter class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.interarearouter.InterAreaRouter)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.interarearouter import InterAreaRouter
        return InterAreaRouter(self)

    @property
    def IntraAreaPrefix(self):
        """An instance of the IntraAreaPrefix class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.intraareaprefix.IntraAreaPrefix)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.intraareaprefix import IntraAreaPrefix
        return IntraAreaPrefix(self)

    @property
    def LinkLsaRoutes(self):
        """An instance of the LinkLsaRoutes class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.linklsaroutes.LinkLsaRoutes)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.linklsaroutes import LinkLsaRoutes
        return LinkLsaRoutes(self)

    @property
    def NssaRoutes(self):
        """An instance of the NssaRoutes class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nssaroutes.NssaRoutes)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nssaroutes import NssaRoutes
        return NssaRoutes(self)

    @property
    def Ospfv3SRGBRangeSubObjectsList(self):
        """An instance of the Ospfv3SRGBRangeSubObjectsList class.

        Returns:
            obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3srgbrangesubobjectslist.Ospfv3SRGBRangeSubObjectsList)

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3srgbrangesubobjectslist import Ospfv3SRGBRangeSubObjectsList
        return Ospfv3SRGBRangeSubObjectsList(self)

    @property
    def Active(self):
        """Activate/Deactivate Configuration

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('active')

    @property
    def Algorithm(self):
        """Algorithm for the Node SID/Label

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('algorithm')

    @property
    def BBit(self):
        """Router-LSA B-Bit

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('bBit')

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
    def EBit(self):
        """Router-LSA E-Bit

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('eBit')

    @property
    def EFlag(self):
        """E Flag: Explicit-Null Flag: If set, any upstream neighbor of the Prefix-SID originator MUST replace the Prefix-SID with a Prefix-SID having an Explicit-NULL value (0 for IPv4 and 2 for IPv6) before forwarding the packet

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('eFlag')

    @property
    def EnableSrMpls(self):
        """Makes the Segment Routing configuration enabled

        Returns:
            bool
        """
        return self._get_attribute('enableSrMpls')
    @EnableSrMpls.setter
    def EnableSrMpls(self, value):
        self._set_attribute('enableSrMpls', value)

    @property
    def LFlag(self):
        """L-Flag: Local Flag. If set, then the value/index carried by the SID has local significance

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('lFlag')

    @property
    def MFlag(self):
        """M-Flag: Mapping Server Flag: If set, the SID was advertised by a Segment Routing Mapping Server

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('mFlag')

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
    def NpFlag(self):
        """NP Flag: No-PHP Flag: If set, then the penultimate hop MUST NOT pop the Prefix-SID before delivering the packet to the node that advertised the Prefix-SID

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('npFlag')

    @property
    def SidIndexLabel(self):
        """SID/Index/Label value associated with the IGP Prefix segment attached to the specific IPv6 prefix

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('sidIndexLabel')

    @property
    def SrgbRangeCount(self):
        """count of the configurable list of SRGB

        Returns:
            number
        """
        return self._get_attribute('srgbRangeCount')
    @SrgbRangeCount.setter
    def SrgbRangeCount(self, value):
        self._set_attribute('srgbRangeCount', value)

    @property
    def VFlag(self):
        """V-Flag: Value flag. If set, then the SID carries an absolute value label value

        Returns:
            obj(ixnetwork_restpy.multivalue.Multivalue)
        """
        return self._get_attribute('vFlag')

    def update(self, EnableSrMpls=None, Name=None, SrgbRangeCount=None):
        """Updates a child instance of ospfv3PseudoRouter on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args:
            EnableSrMpls (bool): Makes the Segment Routing configuration enabled
            Name (str): Name of NGPF element, guaranteed to be unique in Scenario
            SrgbRangeCount (number): count of the configurable list of SRGB

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        self._update(locals())

    def find(self, Count=None, DescriptiveName=None, EnableSrMpls=None, Name=None, SrgbRangeCount=None):
        """Finds and retrieves ospfv3PseudoRouter data from the server.

        All named parameters support regex and can be used to selectively retrieve ospfv3PseudoRouter data from the server.
        By default the find method takes no parameters and will retrieve all ospfv3PseudoRouter data from the server.

        Args:
            Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
            DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
            EnableSrMpls (bool): Makes the Segment Routing configuration enabled
            Name (str): Name of NGPF element, guaranteed to be unique in Scenario
            SrgbRangeCount (number): count of the configurable list of SRGB

        Returns:
            self: This instance with matching ospfv3PseudoRouter data retrieved from the server available through an iterator or index

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(locals())

    def read(self, href):
        """Retrieves a single instance of ospfv3PseudoRouter data from the server.

        Args:
            href (str): An href to the instance to be retrieved

        Returns:
            self: This instance with the ospfv3PseudoRouter data from the server available through an iterator or index

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, Algorithm=None, BBit=None, ConfigureSIDIndexLabel=None, EBit=None, EFlag=None, LFlag=None, MFlag=None, NpFlag=None, SidIndexLabel=None, VFlag=None):
        """Base class infrastructure that gets a list of ospfv3PseudoRouter device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args:
            PortNames (str): optional regex of port names
            Active (str): optional regex of active
            Algorithm (str): optional regex of algorithm
            BBit (str): optional regex of bBit
            ConfigureSIDIndexLabel (str): optional regex of configureSIDIndexLabel
            EBit (str): optional regex of eBit
            EFlag (str): optional regex of eFlag
            LFlag (str): optional regex of lFlag
            MFlag (str): optional regex of mFlag
            NpFlag (str): optional regex of npFlag
            SidIndexLabel (str): optional regex of sidIndexLabel
            VFlag (str): optional regex of vFlag

        Returns:
            list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises:
            ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())

    def Start(self):
        """Executes the start operation on the server.

        Start CPF control plane (equals to promote to negotiated state).

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('start', payload=payload, response_object=None)

    def StartSimulatedRouter(self, *args, **kwargs):
        """Executes the startSimulatedRouter operation on the server.

        Start Pseudo Router

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        startSimulatedRouter()

        startSimulatedRouter(SessionIndices:list)
            Args:
                args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        startSimulatedRouter(SessionIndices:string)
            Args:
                args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        startSimulatedRouter(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the network info. An empty list indicates all instances in the node specific data.

            Returns:
                list(str): ID to associate each async action invocation

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('startSimulatedRouter', payload=payload, response_object=None)

    def Stop(self):
        """Executes the stop operation on the server.

        Stop CPF control plane (equals to demote to PreValidated-DoDDone state).

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        return self._execute('stop', payload=payload, response_object=None)

    def StopSimulatedRouter(self, *args, **kwargs):
        """Executes the stopSimulatedRouter operation on the server.

        Stop Pseudo Router

        The IxNetwork modeling infrastructure allows for multiple method Signatures with the same name while python does not.
        The following correlates the modeling Signatures to the python *args variable length list:

        stopSimulatedRouter()

        stopSimulatedRouter(SessionIndices:list)
            Args:
                args[0] is SessionIndices (list(number)): This parameter requires an array of session numbers 0 1 2 3

        stopSimulatedRouter(SessionIndices:string)
            Args:
                args[0] is SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        stopSimulatedRouter(Arg2:list)list
            Args:
                args[0] is Arg2 (list(number)): List of indices into the network info. An empty list indicates all instances in the network info.

            Returns:
                list(str): ID to associate each async action invocation

        Raises:
            NotFoundError: The requested resource does not exist on the server
            ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stopSimulatedRouter', payload=payload, response_object=None)
