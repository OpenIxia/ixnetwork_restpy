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


class Ospfv3PseudoRouter(Base):
    """Simulated Router Information
    The Ospfv3PseudoRouter class encapsulates a list of ospfv3PseudoRouter resources that are managed by the system.
    A list of resources can be retrieved from the server using the Ospfv3PseudoRouter.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'ospfv3PseudoRouter'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'Algorithm': 'algorithm',
        'BBit': 'bBit',
        'ConfigureSIDIndexLabel': 'configureSIDIndexLabel',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'EBit': 'eBit',
        'EFlag': 'eFlag',
        'EnableSrMpls': 'enableSrMpls',
        'LFlag': 'lFlag',
        'LoopbackAddress': 'loopbackAddress',
        'MFlag': 'mFlag',
        'Name': 'name',
        'NpFlag': 'npFlag',
        'PrefixOptions': 'prefixOptions',
        'SidIndexLabel': 'sidIndexLabel',
        'SrgbRangeCount': 'srgbRangeCount',
        'VFlag': 'vFlag',
    }

    def __init__(self, parent):
        super(Ospfv3PseudoRouter, self).__init__(parent)

    @property
    def ExternalRoutes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.externalroutes_1ced449f46e284c113ae2194af2ffb97.ExternalRoutes): An instance of the ExternalRoutes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.externalroutes_1ced449f46e284c113ae2194af2ffb97 import ExternalRoutes
        return ExternalRoutes(self)

    @property
    def InterAreaPrefix(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.interareaprefix_d5c1af5dfb80980a591c026bbf1a1217.InterAreaPrefix): An instance of the InterAreaPrefix class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.interareaprefix_d5c1af5dfb80980a591c026bbf1a1217 import InterAreaPrefix
        return InterAreaPrefix(self)

    @property
    def InterAreaRouter(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.interarearouter_e3708b9636f21a071f8de5213e1653fb.InterAreaRouter): An instance of the InterAreaRouter class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.interarearouter_e3708b9636f21a071f8de5213e1653fb import InterAreaRouter
        return InterAreaRouter(self)

    @property
    def IntraAreaPrefix(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.intraareaprefix_948ccdbed233cc17b5c5cd2caa82b61f.IntraAreaPrefix): An instance of the IntraAreaPrefix class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.intraareaprefix_948ccdbed233cc17b5c5cd2caa82b61f import IntraAreaPrefix
        return IntraAreaPrefix(self)

    @property
    def LinkLsaRoutes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.linklsaroutes_a80c9071154775869e327a02125984ee.LinkLsaRoutes): An instance of the LinkLsaRoutes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.linklsaroutes_a80c9071154775869e327a02125984ee import LinkLsaRoutes
        return LinkLsaRoutes(self)

    @property
    def NssaRoutes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nssaroutes_ff8ecb21072a534ab3d887c03c4e1cc2.NssaRoutes): An instance of the NssaRoutes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.nssaroutes_ff8ecb21072a534ab3d887c03c4e1cc2 import NssaRoutes
        return NssaRoutes(self)

    @property
    def Ospfv3SRGBRangeSubObjectsList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3srgbrangesubobjectslist_be527e153c8e6d4e5c3f4321aa8409c4.Ospfv3SRGBRangeSubObjectsList): An instance of the Ospfv3SRGBRangeSubObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfv3srgbrangesubobjectslist_be527e153c8e6d4e5c3f4321aa8409c4 import Ospfv3SRGBRangeSubObjectsList
        return Ospfv3SRGBRangeSubObjectsList(self)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/Deactivate Configuration
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def Algorithm(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Algorithm for the Node SID/Label
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Algorithm']))

    @property
    def BBit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Router-LSA B-Bit
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BBit']))

    @property
    def ConfigureSIDIndexLabel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Lets the corresponding router send Prefix SID. By default, it is selected
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ConfigureSIDIndexLabel']))

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
    def EBit(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Router-LSA E-Bit
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EBit']))

    @property
    def EFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): E Flag: Explicit-Null Flag: If set, any upstream neighbor of the Prefix-SID originator MUST replace the Prefix-SID with a Prefix-SID having an Explicit-NULL value (0 for IPv4 and 2 for IPv6) before forwarding the packet
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EFlag']))

    @property
    def EnableSrMpls(self):
        """
        Returns
        -------
        - bool: Makes the Segment Routing configuration enabled
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSrMpls'])
    @EnableSrMpls.setter
    def EnableSrMpls(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSrMpls'], value)

    @property
    def LFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): L-Flag: Local Flag. If set, then the value/index carried by the SID has local significance
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LFlag']))

    @property
    def LoopbackAddress(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Node IPv6 loopback address advertised in Extended Intra Area LSAs by OSPFv3 routers
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LoopbackAddress']))

    @property
    def MFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): M-Flag: Mapping Server Flag: If set, the SID was advertised by a Segment Routing Mapping Server
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MFlag']))

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
    def NpFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): NP Flag: No-PHP Flag: If set, then the penultimate hop MUST NOT pop the Prefix-SID before delivering the packet to the node that advertised the Prefix-SID
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NpFlag']))

    @property
    def PrefixOptions(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Prefix options bits (N, DN, P, x, LA, NU) advertised along with Node Loopback Address in Extended Intra Area LSAs by OSPFv3 routers. Default value is 0x20 which indicates N (Node) bit is set.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['PrefixOptions']))

    @property
    def SidIndexLabel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SID/Index/Label value associated with the IGP Prefix segment attached to the specific IPv6 prefix
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SidIndexLabel']))

    @property
    def SrgbRangeCount(self):
        """
        Returns
        -------
        - number: count of the configurable list of SRGB
        """
        return self._get_attribute(self._SDM_ATT_MAP['SrgbRangeCount'])
    @SrgbRangeCount.setter
    def SrgbRangeCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SrgbRangeCount'], value)

    @property
    def VFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): V-Flag: Value flag. If set, then the SID carries an absolute value label value
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VFlag']))

    def update(self, EnableSrMpls=None, Name=None, SrgbRangeCount=None):
        """Updates ospfv3PseudoRouter resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - EnableSrMpls (bool): Makes the Segment Routing configuration enabled
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SrgbRangeCount (number): count of the configurable list of SRGB

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, EnableSrMpls=None, Name=None, SrgbRangeCount=None):
        """Finds and retrieves ospfv3PseudoRouter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ospfv3PseudoRouter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ospfv3PseudoRouter resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - EnableSrMpls (bool): Makes the Segment Routing configuration enabled
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SrgbRangeCount (number): count of the configurable list of SRGB

        Returns
        -------
        - self: This instance with matching ospfv3PseudoRouter resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ospfv3PseudoRouter data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ospfv3PseudoRouter resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, Algorithm=None, BBit=None, ConfigureSIDIndexLabel=None, EBit=None, EFlag=None, LFlag=None, LoopbackAddress=None, MFlag=None, NpFlag=None, PrefixOptions=None, SidIndexLabel=None, VFlag=None):
        """Base class infrastructure that gets a list of ospfv3PseudoRouter device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - Algorithm (str): optional regex of algorithm
        - BBit (str): optional regex of bBit
        - ConfigureSIDIndexLabel (str): optional regex of configureSIDIndexLabel
        - EBit (str): optional regex of eBit
        - EFlag (str): optional regex of eFlag
        - LFlag (str): optional regex of lFlag
        - LoopbackAddress (str): optional regex of loopbackAddress
        - MFlag (str): optional regex of mFlag
        - NpFlag (str): optional regex of npFlag
        - PrefixOptions (str): optional regex of prefixOptions
        - SidIndexLabel (str): optional regex of sidIndexLabel
        - VFlag (str): optional regex of vFlag

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

    def StartSimulatedRouter(self, *args, **kwargs):
        """Executes the startSimulatedRouter operation on the server.

        Start Pseudo Router

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        startSimulatedRouter(SessionIndices=list)
        -----------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        startSimulatedRouter(SessionIndices=string)
        -------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        startSimulatedRouter(Arg2=list)list
        -----------------------------------
        - Arg2 (list(number)): List of indices into the network info. An empty list indicates all instances in the node specific data.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('startSimulatedRouter', payload=payload, response_object=None)

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

    def StopSimulatedRouter(self, *args, **kwargs):
        """Executes the stopSimulatedRouter operation on the server.

        Stop Pseudo Router

        The IxNetwork model allows for multiple method Signatures with the same name while python does not.

        stopSimulatedRouter(SessionIndices=list)
        ----------------------------------------
        - SessionIndices (list(number)): This parameter requires an array of session numbers 1 2 3

        stopSimulatedRouter(SessionIndices=string)
        ------------------------------------------
        - SessionIndices (str): This parameter requires a string of session numbers 1-4;6;7-12

        stopSimulatedRouter(Arg2=list)list
        ----------------------------------
        - Arg2 (list(number)): List of indices into the network info. An empty list indicates all instances in the network info.
        - Returns list(str): ID to associate each async action invocation

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stopSimulatedRouter', payload=payload, response_object=None)
