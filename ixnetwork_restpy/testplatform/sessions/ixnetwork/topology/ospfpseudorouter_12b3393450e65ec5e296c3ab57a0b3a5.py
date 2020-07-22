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


class OspfPseudoRouter(Base):
    """Simulated Router Information
    The OspfPseudoRouter class encapsulates a list of ospfPseudoRouter resources that are managed by the system.
    A list of resources can be retrieved from the server using the OspfPseudoRouter.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'ospfPseudoRouter'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'AdvertiseRouterIdAsStubNetwork': 'advertiseRouterIdAsStubNetwork',
        'Algorithm': 'algorithm',
        'BBit': 'bBit',
        'ConfigureSIDIndexLabel': 'configureSIDIndexLabel',
        'Count': 'count',
        'DescriptiveName': 'descriptiveName',
        'EBit': 'eBit',
        'EFlag': 'eFlag',
        'EnableSegmentRouting': 'enableSegmentRouting',
        'EnableSrlb': 'enableSrlb',
        'LFlag': 'lFlag',
        'MFlag': 'mFlag',
        'Name': 'name',
        'NpFlag': 'npFlag',
        'SRAlgorithmCount': 'sRAlgorithmCount',
        'SidIndexLabel': 'sidIndexLabel',
        'SrgbRangeCount': 'srgbRangeCount',
        'SrlbRangeCount': 'srlbRangeCount',
        'VFlag': 'vFlag',
    }

    def __init__(self, parent):
        super(OspfPseudoRouter, self).__init__(parent)

    @property
    def OspfPseudoRouterStubNetworks(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfpseudorouterstubnetworks_529623b7b4a99bce259e7e9cc31d4740.OspfPseudoRouterStubNetworks): An instance of the OspfPseudoRouterStubNetworks class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfpseudorouterstubnetworks_529623b7b4a99bce259e7e9cc31d4740 import OspfPseudoRouterStubNetworks
        return OspfPseudoRouterStubNetworks(self)

    @property
    def OspfPseudoRouterStubRoutes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfpseudorouterstubroutes_412e064d08a94b4fcc40c44dd11c5318.OspfPseudoRouterStubRoutes): An instance of the OspfPseudoRouterStubRoutes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfpseudorouterstubroutes_412e064d08a94b4fcc40c44dd11c5318 import OspfPseudoRouterStubRoutes
        return OspfPseudoRouterStubRoutes(self)

    @property
    def OspfPseudoRouterSummaryRoutes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfpseudoroutersummaryroutes_5e51c97c0564d672f57ec5fd0f34b1cb.OspfPseudoRouterSummaryRoutes): An instance of the OspfPseudoRouterSummaryRoutes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfpseudoroutersummaryroutes_5e51c97c0564d672f57ec5fd0f34b1cb import OspfPseudoRouterSummaryRoutes
        return OspfPseudoRouterSummaryRoutes(self)

    @property
    def OspfPseudoRouterType1ExtRoutes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfpseudoroutertype1extroutes_8af6c2f32014611d60e64f734921e6df.OspfPseudoRouterType1ExtRoutes): An instance of the OspfPseudoRouterType1ExtRoutes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfpseudoroutertype1extroutes_8af6c2f32014611d60e64f734921e6df import OspfPseudoRouterType1ExtRoutes
        return OspfPseudoRouterType1ExtRoutes(self)

    @property
    def OspfPseudoRouterType2ExtRoutes(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfpseudoroutertype2extroutes_1eb6898acd2430328b24bfa765a4dc59.OspfPseudoRouterType2ExtRoutes): An instance of the OspfPseudoRouterType2ExtRoutes class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfpseudoroutertype2extroutes_1eb6898acd2430328b24bfa765a4dc59 import OspfPseudoRouterType2ExtRoutes
        return OspfPseudoRouterType2ExtRoutes(self)

    @property
    def OspfSRAlgorithmList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfsralgorithmlist_6d5b092154ba202ff142c9a80bdf1352.OspfSRAlgorithmList): An instance of the OspfSRAlgorithmList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfsralgorithmlist_6d5b092154ba202ff142c9a80bdf1352 import OspfSRAlgorithmList
        return OspfSRAlgorithmList(self)

    @property
    def OspfSRGBRangeSubObjectsList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfsrgbrangesubobjectslist_3183939e699e6d81694733106246396f.OspfSRGBRangeSubObjectsList): An instance of the OspfSRGBRangeSubObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfsrgbrangesubobjectslist_3183939e699e6d81694733106246396f import OspfSRGBRangeSubObjectsList
        return OspfSRGBRangeSubObjectsList(self)

    @property
    def OspfSRLBRangeSubObjectsList(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfsrlbrangesubobjectslist_3469b01175113efcd50b58a826370e91.OspfSRLBRangeSubObjectsList): An instance of the OspfSRLBRangeSubObjectsList class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfsrlbrangesubobjectslist_3469b01175113efcd50b58a826370e91 import OspfSRLBRangeSubObjectsList
        return OspfSRLBRangeSubObjectsList(self)

    @property
    def Active(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/DeActivate OSPF Simulated Router
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def AdvertiseRouterIdAsStubNetwork(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise RouterId As Stub Network
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseRouterIdAsStubNetwork']))

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
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure SID/Index/Label
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
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
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
        - obj(ixnetwork_restpy.multivalue.Multivalue): Explicit-Null Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EFlag']))

    @property
    def EnableSegmentRouting(self):
        """
        Returns
        -------
        - bool: Enable Segment Routing
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSegmentRouting'])
    @EnableSegmentRouting.setter
    def EnableSegmentRouting(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSegmentRouting'], value)

    @property
    def EnableSrlb(self):
        """
        Returns
        -------
        - bool: Enable SRLB
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSrlb'])
    @EnableSrlb.setter
    def EnableSrlb(self, value):
        self._set_attribute(self._SDM_ATT_MAP['EnableSrlb'], value)

    @property
    def LFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Local or Global Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LFlag']))

    @property
    def MFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Mapping Server Flag
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
        - obj(ixnetwork_restpy.multivalue.Multivalue): No-PHP Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NpFlag']))

    @property
    def SRAlgorithmCount(self):
        """
        Returns
        -------
        - number: SR Algorithm Count
        """
        return self._get_attribute(self._SDM_ATT_MAP['SRAlgorithmCount'])
    @SRAlgorithmCount.setter
    def SRAlgorithmCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SRAlgorithmCount'], value)

    @property
    def SidIndexLabel(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SID/Index/Label
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SidIndexLabel']))

    @property
    def SrgbRangeCount(self):
        """
        Returns
        -------
        - number: SRGB Range Count
        """
        return self._get_attribute(self._SDM_ATT_MAP['SrgbRangeCount'])
    @SrgbRangeCount.setter
    def SrgbRangeCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SrgbRangeCount'], value)

    @property
    def SrlbRangeCount(self):
        """
        Returns
        -------
        - number: SRLB Range Count
        """
        return self._get_attribute(self._SDM_ATT_MAP['SrlbRangeCount'])
    @SrlbRangeCount.setter
    def SrlbRangeCount(self, value):
        self._set_attribute(self._SDM_ATT_MAP['SrlbRangeCount'], value)

    @property
    def VFlag(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Value or Index Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VFlag']))

    def update(self, EnableSegmentRouting=None, EnableSrlb=None, Name=None, SRAlgorithmCount=None, SrgbRangeCount=None, SrlbRangeCount=None):
        """Updates ospfPseudoRouter resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - EnableSegmentRouting (bool): Enable Segment Routing
        - EnableSrlb (bool): Enable SRLB
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SRAlgorithmCount (number): SR Algorithm Count
        - SrgbRangeCount (number): SRGB Range Count
        - SrlbRangeCount (number): SRLB Range Count

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, EnableSegmentRouting=None, EnableSrlb=None, Name=None, SRAlgorithmCount=None, SrgbRangeCount=None, SrlbRangeCount=None):
        """Finds and retrieves ospfPseudoRouter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ospfPseudoRouter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ospfPseudoRouter resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offers more context
        - EnableSegmentRouting (bool): Enable Segment Routing
        - EnableSrlb (bool): Enable SRLB
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - SRAlgorithmCount (number): SR Algorithm Count
        - SrgbRangeCount (number): SRGB Range Count
        - SrlbRangeCount (number): SRLB Range Count

        Returns
        -------
        - self: This instance with matching ospfPseudoRouter resources retrieved from the server available through an iterator or index

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._select(self._map_locals(self._SDM_ATT_MAP, locals()))

    def read(self, href):
        """Retrieves a single instance of ospfPseudoRouter data from the server.

        Args
        ----
        - href (str): An href to the instance to be retrieved

        Returns
        -------
        - self: This instance with the ospfPseudoRouter resources from the server available through an iterator or index

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._read(href)

    def get_device_ids(self, PortNames=None, Active=None, AdvertiseRouterIdAsStubNetwork=None, Algorithm=None, BBit=None, ConfigureSIDIndexLabel=None, EBit=None, EFlag=None, LFlag=None, MFlag=None, NpFlag=None, SidIndexLabel=None, VFlag=None):
        """Base class infrastructure that gets a list of ospfPseudoRouter device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AdvertiseRouterIdAsStubNetwork (str): optional regex of advertiseRouterIdAsStubNetwork
        - Algorithm (str): optional regex of algorithm
        - BBit (str): optional regex of bBit
        - ConfigureSIDIndexLabel (str): optional regex of configureSIDIndexLabel
        - EBit (str): optional regex of eBit
        - EFlag (str): optional regex of eFlag
        - LFlag (str): optional regex of lFlag
        - MFlag (str): optional regex of mFlag
        - NpFlag (str): optional regex of npFlag
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
