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
from typing import List, Any, Union


class OspfPseudoRouter(Base):
    """Simulated Router Information
    The OspfPseudoRouter class encapsulates a list of ospfPseudoRouter resources that are managed by the system.
    A list of resources can be retrieved from the server using the OspfPseudoRouter.find() method.
    """

    __slots__ = ()
    _SDM_NAME = 'ospfPseudoRouter'
    _SDM_ATT_MAP = {
        'Active': 'active',
        'AdvertiseFapm': 'advertiseFapm',
        'AdvertiseRouterIdAsStubNetwork': 'advertiseRouterIdAsStubNetwork',
        'Algorithm': 'algorithm',
        'BBit': 'bBit',
        'ConfigureSIDIndexLabel': 'configureSIDIndexLabel',
        'Count': 'count',
        'DemandCircuit': 'demandCircuit',
        'DescriptiveName': 'descriptiveName',
        'EBit': 'eBit',
        'EFlag': 'eFlag',
        'EnableSegmentRouting': 'enableSegmentRouting',
        'EnableSrlb': 'enableSrlb',
        'ExtendedPrefixFlags': 'extendedPrefixFlags',
        'ExternalAttribute': 'externalAttribute',
        'ExternalCapability': 'externalCapability',
        'FapmMetric': 'fapmMetric',
        'LFlag': 'lFlag',
        'MFlag': 'mFlag',
        'MulticastCapability': 'multicastCapability',
        'Name': 'name',
        'NoOfAddiotnalAlgoSidCount': 'noOfAddiotnalAlgoSidCount',
        'NpFlag': 'npFlag',
        'NssaCapability': 'nssaCapability',
        'OpaqueLsaForwarded': 'opaqueLsaForwarded',
        'SRAlgorithmCount': 'sRAlgorithmCount',
        'SidIndexLabel': 'sidIndexLabel',
        'SrgbRangeCount': 'srgbRangeCount',
        'SrlbRangeCount': 'srlbRangeCount',
        'TypeOfServiceRouting': 'typeOfServiceRouting',
        'Unused': 'unused',
        'VFlag': 'vFlag',
    }
    _SDM_ENUM_MAP = {
    }

    def __init__(self, parent, list_op=False):
        super(OspfPseudoRouter, self).__init__(parent, list_op)

    @property
    def OspfPseudoPrefixesSid(self):
        """
        Returns
        -------
        - obj(ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfpseudoprefixessid_3b1ec47376666bd4309a78f3999c54d1.OspfPseudoPrefixesSid): An instance of the OspfPseudoPrefixesSid class

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        from ixnetwork_restpy.testplatform.sessions.ixnetwork.topology.ospfpseudoprefixessid_3b1ec47376666bd4309a78f3999c54d1 import OspfPseudoPrefixesSid
        if self._properties.get('OspfPseudoPrefixesSid', None) is not None:
            return self._properties.get('OspfPseudoPrefixesSid')
        else:
            return OspfPseudoPrefixesSid(self)._select()

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
        if self._properties.get('OspfPseudoRouterStubNetworks', None) is not None:
            return self._properties.get('OspfPseudoRouterStubNetworks')
        else:
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
        if self._properties.get('OspfPseudoRouterStubRoutes', None) is not None:
            return self._properties.get('OspfPseudoRouterStubRoutes')
        else:
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
        if self._properties.get('OspfPseudoRouterSummaryRoutes', None) is not None:
            return self._properties.get('OspfPseudoRouterSummaryRoutes')
        else:
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
        if self._properties.get('OspfPseudoRouterType1ExtRoutes', None) is not None:
            return self._properties.get('OspfPseudoRouterType1ExtRoutes')
        else:
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
        if self._properties.get('OspfPseudoRouterType2ExtRoutes', None) is not None:
            return self._properties.get('OspfPseudoRouterType2ExtRoutes')
        else:
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
        if self._properties.get('OspfSRAlgorithmList', None) is not None:
            return self._properties.get('OspfSRAlgorithmList')
        else:
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
        if self._properties.get('OspfSRGBRangeSubObjectsList', None) is not None:
            return self._properties.get('OspfSRGBRangeSubObjectsList')
        else:
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
        if self._properties.get('OspfSRLBRangeSubObjectsList', None) is not None:
            return self._properties.get('OspfSRLBRangeSubObjectsList')
        else:
            return OspfSRLBRangeSubObjectsList(self)

    @property
    def Active(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Activate/DeActivate OSPF Simulated Router
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Active']))

    @property
    def AdvertiseFapm(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise FAPM
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseFapm']))

    @property
    def AdvertiseRouterIdAsStubNetwork(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Advertise RouterId As Stub Network
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['AdvertiseRouterIdAsStubNetwork']))

    @property
    def Algorithm(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Algorithm for the Node SID/Label
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Algorithm']))

    @property
    def BBit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Router-LSA B-Bit
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['BBit']))

    @property
    def ConfigureSIDIndexLabel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Configure SID/Index/Label
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ConfigureSIDIndexLabel']))

    @property
    def Count(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        """
        return self._get_attribute(self._SDM_ATT_MAP['Count'])

    @property
    def DemandCircuit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Option bit 5 : The DC-Bit should be set in all LSAs originated by Router implementing the Demand Circuit functionality.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['DemandCircuit']))

    @property
    def DescriptiveName(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        """
        return self._get_attribute(self._SDM_ATT_MAP['DescriptiveName'])

    @property
    def EBit(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Router-LSA E-Bit
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EBit']))

    @property
    def EFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Explicit-Null Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['EFlag']))

    @property
    def EnableSegmentRouting(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable Segment Routing
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSegmentRouting'])
    @EnableSegmentRouting.setter
    def EnableSegmentRouting(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableSegmentRouting'], value)

    @property
    def EnableSrlb(self):
        # type: () -> bool
        """
        Returns
        -------
        - bool: Enable SRLB
        """
        return self._get_attribute(self._SDM_ATT_MAP['EnableSrlb'])
    @EnableSrlb.setter
    def EnableSrlb(self, value):
        # type: (bool) -> None
        self._set_attribute(self._SDM_ATT_MAP['EnableSrlb'], value)

    @property
    def ExtendedPrefixFlags(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Extended prefix flags advertised along with Node Loopback Address in Extended Prefix TLV by OSPFv2 routers. This is a hex field. The default value is 0x40. 0x40 signifies Node flag (N flag) is set.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ExtendedPrefixFlags']))

    @property
    def ExternalAttribute(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Option bit 4 : The EA-bit describes the router's willingness to receive and forward External-Attributes-LSAs.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ExternalAttribute']))

    @property
    def ExternalCapability(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Option bit 1 : The E-bit represents OSPF's ExternalRoutingCapability. This bit can be set in all LSAs associated with the backbone, non-stub areas and AS-external-LSAs.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['ExternalCapability']))

    @property
    def FapmMetric(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): FAPM Metric
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['FapmMetric']))

    @property
    def LFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Local or Global Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['LFlag']))

    @property
    def MFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Mapping Server Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MFlag']))

    @property
    def MulticastCapability(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Option bit 2 : The MC-bit describes the multicast capability of the various pieces of the OSPF routing domain.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['MulticastCapability']))

    @property
    def Name(self):
        # type: () -> str
        """
        Returns
        -------
        - str: Name of NGPF element, guaranteed to be unique in Scenario
        """
        return self._get_attribute(self._SDM_ATT_MAP['Name'])
    @Name.setter
    def Name(self, value):
        # type: (str) -> None
        self._set_attribute(self._SDM_ATT_MAP['Name'], value)

    @property
    def NoOfAddiotnalAlgoSidCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: Additional Algo/SID Count
        """
        return self._get_attribute(self._SDM_ATT_MAP['NoOfAddiotnalAlgoSidCount'])
    @NoOfAddiotnalAlgoSidCount.setter
    def NoOfAddiotnalAlgoSidCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['NoOfAddiotnalAlgoSidCount'], value)

    @property
    def NpFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): No-PHP Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NpFlag']))

    @property
    def NssaCapability(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Option bit 3 : The N/P-bit used only in the Type-7 LSA header. It flags the NSSA border router to translate the Type-7 LSA into a Type-5 LSA.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['NssaCapability']))

    @property
    def OpaqueLsaForwarded(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Option bit 6: The O-bit describes the router's willingness to receive and forward Opaque LSAs.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['OpaqueLsaForwarded']))

    @property
    def SRAlgorithmCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: SR Algorithm Count
        """
        return self._get_attribute(self._SDM_ATT_MAP['SRAlgorithmCount'])
    @SRAlgorithmCount.setter
    def SRAlgorithmCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['SRAlgorithmCount'], value)

    @property
    def SidIndexLabel(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): SID/Index/Label
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['SidIndexLabel']))

    @property
    def SrgbRangeCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: SRGB Range Count
        """
        return self._get_attribute(self._SDM_ATT_MAP['SrgbRangeCount'])
    @SrgbRangeCount.setter
    def SrgbRangeCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['SrgbRangeCount'], value)

    @property
    def SrlbRangeCount(self):
        # type: () -> int
        """
        Returns
        -------
        - number: SRLB Range Count
        """
        return self._get_attribute(self._SDM_ATT_MAP['SrlbRangeCount'])
    @SrlbRangeCount.setter
    def SrlbRangeCount(self, value):
        # type: (int) -> None
        self._set_attribute(self._SDM_ATT_MAP['SrlbRangeCount'], value)

    @property
    def TypeOfServiceRouting(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Option bit 0 : The T-bit represents OSPF's TOS routing capability.
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['TypeOfServiceRouting']))

    @property
    def Unused(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Option bit 7 (Unused).
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['Unused']))

    @property
    def VFlag(self):
        # type: () -> 'Multivalue'
        """
        Returns
        -------
        - obj(ixnetwork_restpy.multivalue.Multivalue): Value or Index Flag
        """
        from ixnetwork_restpy.multivalue import Multivalue
        return Multivalue(self, self._get_attribute(self._SDM_ATT_MAP['VFlag']))

    def update(self, EnableSegmentRouting=None, EnableSrlb=None, Name=None, NoOfAddiotnalAlgoSidCount=None, SRAlgorithmCount=None, SrgbRangeCount=None, SrlbRangeCount=None):
        # type: (bool, bool, str, int, int, int, int) -> OspfPseudoRouter
        """Updates ospfPseudoRouter resource on the server.

        This method has some named parameters with a type: obj (Multivalue).
        The Multivalue class has documentation that details the possible values for those named parameters.

        Args
        ----
        - EnableSegmentRouting (bool): Enable Segment Routing
        - EnableSrlb (bool): Enable SRLB
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfAddiotnalAlgoSidCount (number): Additional Algo/SID Count
        - SRAlgorithmCount (number): SR Algorithm Count
        - SrgbRangeCount (number): SRGB Range Count
        - SrlbRangeCount (number): SRLB Range Count

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._update(self._map_locals(self._SDM_ATT_MAP, locals()))

    def add(self, EnableSegmentRouting=None, EnableSrlb=None, Name=None, NoOfAddiotnalAlgoSidCount=None, SRAlgorithmCount=None, SrgbRangeCount=None, SrlbRangeCount=None):
        # type: (bool, bool, str, int, int, int, int) -> OspfPseudoRouter
        """Adds a new ospfPseudoRouter resource on the json, only valid with config assistant

        Args
        ----
        - EnableSegmentRouting (bool): Enable Segment Routing
        - EnableSrlb (bool): Enable SRLB
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfAddiotnalAlgoSidCount (number): Additional Algo/SID Count
        - SRAlgorithmCount (number): SR Algorithm Count
        - SrgbRangeCount (number): SRGB Range Count
        - SrlbRangeCount (number): SRLB Range Count

        Returns
        -------
        - self: This instance with all currently retrieved ospfPseudoRouter resources using find and the newly added ospfPseudoRouter resources available through an iterator or index

        Raises
        ------
        - Exception: if this function is not being used with config assistance
        """
        return self._add_xpath(self._map_locals(self._SDM_ATT_MAP, locals()))

    def find(self, Count=None, DescriptiveName=None, EnableSegmentRouting=None, EnableSrlb=None, Name=None, NoOfAddiotnalAlgoSidCount=None, SRAlgorithmCount=None, SrgbRangeCount=None, SrlbRangeCount=None):
        # type: (int, str, bool, bool, str, int, int, int, int) -> OspfPseudoRouter
        """Finds and retrieves ospfPseudoRouter resources from the server.

        All named parameters are evaluated on the server using regex. The named parameters can be used to selectively retrieve ospfPseudoRouter resources from the server.
        To retrieve an exact match ensure the parameter value starts with ^ and ends with $
        By default the find method takes no parameters and will retrieve all ospfPseudoRouter resources from the server.

        Args
        ----
        - Count (number): Number of elements inside associated multiplier-scaled container object, e.g. number of devices inside a Device Group.
        - DescriptiveName (str): Longer, more descriptive name for element. It's not guaranteed to be unique like -name-, but may offer more context.
        - EnableSegmentRouting (bool): Enable Segment Routing
        - EnableSrlb (bool): Enable SRLB
        - Name (str): Name of NGPF element, guaranteed to be unique in Scenario
        - NoOfAddiotnalAlgoSidCount (number): Additional Algo/SID Count
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

    def Abort(self, *args, **kwargs):
        # type: (*Any, **Any) -> None
        """Executes the abort operation on the server.

        Abort CPF control plane (equals to demote to kUnconfigured state).

        abort(async_operation=bool)
        ---------------------------
        - async_operation (bool=False): True to execute the operation asynchronously. Any subsequent rest api calls made through the Connection class will block until the operation is complete.

        Raises
        ------
        - NotFoundError: The requested resource does not exist on the server
        - ServerError: The server has encountered an uncategorized error condition
        """
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('abort', payload=payload, response_object=None)

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
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('start', payload=payload, response_object=None)

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
        payload = { "Arg1": self }
        for i in range(len(args)): payload['Arg%s' % (i + 2)] = args[i]
        for item in kwargs.items(): payload[item[0]] = item[1]
        return self._execute('stop', payload=payload, response_object=None)

    def get_device_ids(self, PortNames=None, Active=None, AdvertiseFapm=None, AdvertiseRouterIdAsStubNetwork=None, Algorithm=None, BBit=None, ConfigureSIDIndexLabel=None, DemandCircuit=None, EBit=None, EFlag=None, ExtendedPrefixFlags=None, ExternalAttribute=None, ExternalCapability=None, FapmMetric=None, LFlag=None, MFlag=None, MulticastCapability=None, NpFlag=None, NssaCapability=None, OpaqueLsaForwarded=None, SidIndexLabel=None, TypeOfServiceRouting=None, Unused=None, VFlag=None):
        """Base class infrastructure that gets a list of ospfPseudoRouter device ids encapsulated by this object.

        Use the optional regex parameters in the method to refine the list of device ids encapsulated by this object.

        Args
        ----
        - PortNames (str): optional regex of port names
        - Active (str): optional regex of active
        - AdvertiseFapm (str): optional regex of advertiseFapm
        - AdvertiseRouterIdAsStubNetwork (str): optional regex of advertiseRouterIdAsStubNetwork
        - Algorithm (str): optional regex of algorithm
        - BBit (str): optional regex of bBit
        - ConfigureSIDIndexLabel (str): optional regex of configureSIDIndexLabel
        - DemandCircuit (str): optional regex of demandCircuit
        - EBit (str): optional regex of eBit
        - EFlag (str): optional regex of eFlag
        - ExtendedPrefixFlags (str): optional regex of extendedPrefixFlags
        - ExternalAttribute (str): optional regex of externalAttribute
        - ExternalCapability (str): optional regex of externalCapability
        - FapmMetric (str): optional regex of fapmMetric
        - LFlag (str): optional regex of lFlag
        - MFlag (str): optional regex of mFlag
        - MulticastCapability (str): optional regex of multicastCapability
        - NpFlag (str): optional regex of npFlag
        - NssaCapability (str): optional regex of nssaCapability
        - OpaqueLsaForwarded (str): optional regex of opaqueLsaForwarded
        - SidIndexLabel (str): optional regex of sidIndexLabel
        - TypeOfServiceRouting (str): optional regex of typeOfServiceRouting
        - Unused (str): optional regex of unused
        - VFlag (str): optional regex of vFlag

        Returns
        -------
        - list(int): A list of device ids that meets the regex criteria provided in the method parameters

        Raises
        ------
        - ServerError: The server has encountered an uncategorized error condition
        """
        return self._get_ngpf_device_ids(locals())
